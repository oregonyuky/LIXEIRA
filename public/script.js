const API_URL = "http://localhost:5000";

function carregarAposentados() {
    fetch(`${API_URL}/aposentados`)
        .then(res => res.json())
        .then(aposentados => {
            const lista = document.getElementById('lista');
            lista.innerHTML = '';

            aposentados.forEach(ap => {
                const div = document.createElement('div');
                div.innerHTML = `
                    <p><strong>Nome:</strong> ${ap.nome}</p>
                    <p><strong>CPF:</strong> ${ap.cpf}</p>
                    <button onclick="verificarDesconto(${ap.id}, '${ap.cpf}', '${ap.nome}')">Verificar Desconto</button>
                    <hr>
                `;
                lista.appendChild(div);
            });
        });
}

function verificarDesconto(id, cpf, nome) {
    fetch(`${API_URL}/descontos?id=${cpf}`)
        .then(res => res.json())
        .then(descontos => {
            if (descontos.length > 0) {
                const desconto = descontos[0];
                const confirma = confirm(`Existe desconto para ${nome} na associação ${desconto.associacao} no valor de R$ ${desconto.valor}. Deseja cancelar?`);

                if (confirma) {
                    fetch(`${API_URL}/descontos/${desconto.id}`, {
                        method: 'DELETE'
                    })
                    .then(() => {
                        const dataCancelamento = new Date().toLocaleDateString('pt-BR');
                        return fetch(`${API_URL}/cancelamentos`, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                aposentado: cpf,
                                dataCancelamento: dataCancelamento,
                                nome: desconto.associacao,
                                valor: desconto.valor
                            })
                        });
                    })
                    .then(() => {
                        alert("Desconto cancelado e registrado com sucesso.");
                    });
                }
            } else {
                alert("Não existe desconto para este aposentado/pensionista.");
            }
        });
}

function logout() {
    window.location.href = '/logout';
}

carregarAposentados();
