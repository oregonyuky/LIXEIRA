import express from "express";
import session from "express-session";
import path from "path";

const app = express();
const PORT = 4000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Configurar sessão
app.use(session({
  secret: "segredo-super-secreto",
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 600000 } // 10 minutos
}));

// Middleware para proteger rotas
function verificarAutenticacao(req, res, next) {
  if (req.session.usuario) {
    next();
  } else {
    res.redirect("/login");
  }
}

// Servir arquivos estáticos
app.use(express.static(path.join(process.cwd(), "public")));

// Rotas públicas
app.get("/login", (req, res) => {
console.log('POST /login recebido');
  res.sendFile(path.join(process.cwd(), "public/login.html"));
});

app.post("/login", (req, res) => {
  const { usuario, senha } = req.body;
  // Aqui coloque sua regra de autenticação simples
  if (usuario === "funcionario" && senha === "1234") {
    req.session.usuario = usuario;
    res.redirect("/listagem");
  } else {
    res.send("Usuário ou senha inválidos");
  }
});

// Tela protegida
app.get("/listagem", verificarAutenticacao, (req, res) => {
  res.sendFile(path.join(process.cwd(), "public/listagem.html"));
});

// Logout
app.get("/logout", (req, res) => {
  req.session.destroy();
  res.redirect("/login");
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
