### Autor: Fábio Delgado

Olá! Seja bem vindo ;)


## Índice
1. [FlaskApp](#FlaskApp)
2. [Projeto e Conteúdo](#Projeto-e-Conteudo)
3. [Swagger](#Swagger)
4. [JWT](#JWT)
5. [SQL Server e pyodbc](#SQL-Server-e-pyodbc)
6. [Testes unitários (unittest e coverage)](#Testes-unitrios-unittest-e-coverage))
7. [Publicação](#Publicação)
8. [Suporte](#Suporte)

## FlaskApp

Este repositório contém um exemplo de APIs REST com Flask e Python utilizado SQL Server para armazenameto de dados

### Utilize os comandos abaixo para executar a aplicação:

```shell
git clone https://github.com/fabiodelgadopereira/FlaskApp
cd FlaskApp
git checkout almost_perfect
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Como executar essa aplicação?
```shell
python run.py
# ou se quiser alterar a instancia de configuraçṍes
python run.py production
```

4. A aplicação deverá estar disponivel em seu navegador no endereço: http://localhost:5000/swagger

![GitHub Logo](/img/Capturar.png)

### Extensões recomendadas para desenvolvimento no VSCODE

- Python from Microsoft
- Python Docstring Generator from  Nils Werner
- Pyright from  ms-pyright

## Projeto e Conteúdo

Flask é um micro framework da web escrito em Python. É classificado como uma Microframework porque não requer ferramentas ou bibliotecas específicas. Não possui camada de abstração de banco de dados, validação de formulário ou qualquer outro componente em que bibliotecas de terceiros pré-existentes forneçam funções comuns. No entanto, o Flask suporta extensões que podem adicionar recursos de aplicativos como se fossem implementados no próprio Flask. Existem extensões para mapeadores objeto-relacionais, validação de formulários, manipulação de upload, várias tecnologias de autenticação aberta e várias ferramentas comuns relacionadas à estrutura. As extensões são atualizadas pela comunidade com muita frequência.

O Flask-RESTful é uma extensão do Flask que adiciona suporte para a criação rápida de APIs REST. É uma abstração leve que funciona com as bibliotecas ORM/libraries. O RESTful do Flask incentiva as práticas recomendadas com configuração mínima. Se você está familiarizado com o Flask, o Flask-RESTful deve ser de fácil compreensão.

### Entedento a estrutura de projeto de uma aplicação Flask

![GitHub Logo](/img/estrutura.png)

Os arquivos `.gitignore` e  `README.md` são arquivos para gerenciamento de arquivos e documentação de código, não vou entrar em detalhes neste artigo.

A pasta `script` contém o código SQL utilizado para criar o banco de dados e as tabelas dessa aplicação, eles implementam boas práticas de log e execução de script.

Este arquivo `requirements.txt` é usado para especificar quais pacotes python são necessários para executar o projeto que você está visualizando. Normalmente, o arquivo está localizado no diretório raiz do seu projeto. Quando um arquivo com esse nome é adicionado ao diretório raiz do projeto, ele é detectado automaticamente pela Python Integrated tools.

`run.py` será o responsável por iniciar o servidor do Flask. Ele recebe por parâmetro o ambiente em que a aplicação será executada. Passando vazio (sem parâmetro) será executado em modo **development**, caso seja enviado production será executado em modo **production**

Dentro da pasta cadastro estão localizados os principais arquivos da aplicação. No Flask, você tem rotas (URLs) definidas como  function decorators para a application ou blueprint; portanto, no arquivo `routes.py` é definido a funcionalidade para URLs diferentes.

`db.py` contém as informações para conexão com o banco de dados.

Gerenciar estes múltiplos ambientes requer acima de tudo muita disciplina, a Regra N.1 deverá ser seguida a risca, ou seja, NUNCA faça configurações no modo HARD CODED, sempre utilize variáveis de settings para coisas que se alteram entre diferentes ambientes e o arquivo `default_settings.py` armazena valores fixos para os diversos ambientes.

As pastas `development_instance` e `production_instance` possuem versões diferentes do arquivo `config.cfg`. Esse arquivo armazenar os valores de variáveis dos diferentes ambientes da aplicação. É comum encontrar informações como nome da aplicação, porta, flags e caminhos de diretório.

A pasta `Resource` possui o código fonte da aplicação. Esse conteúdo varia conforme escopo da aplicação.

## Swagger

O Swagger é uma aplicação open source que auxilia os desenvolvedores a definir, criar, documentar e consumir APIs REST;
É composto de um arquivo de configuração, que pode ser definido em YAML ou JSON;
Fornece ferramentas para: auxiliar na definição do arquivo de configuração (Swagger Editor), interagir com API através das definições do arquivo de configuração (Swagger UI) e gerar templates de código a partir do arquivo de configuração (Swagger Codegen).

fonte: https://swagger.io/resources/webinars/getting-started-with-swagger/

> A maneira mais fácil de instalar é usar o pip:

```shell
pip install flask_swagger_ui
```
> Exemplo de implementação para testes
```python
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL para expor o Swagger UI (sem colocar '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  #URL exemplo (é claro que pode ser um recurso local)

# Chamada da factory function para criar o blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Os arquivos estáticos da Swagger UI serão mapeados para '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config pode ser substituido
        'app_name': "Test application"
    })

# Registrar o blueprint na URL
# (O URL deve corresponder ao fornecido para a factory function acima)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.run()

# Agora abra seu navegador no endereço: localhost:5000/api/docs/
```

## JWT
O JWT (JSON Web Token) nada mais é que um padrão (RFC-7519) de mercado que define como transmitir e armazenar objetos JSON de forma simples, compacta e segura entre diferentes aplicações, muito utilizado para validar serviços em Web Services pois os dados contidos no token gerado pode ser validado a qualquer momento uma vez que ele é assinado digitalmente.

JSON Web Tokens (JWT) é um padrão stateless porque o servidor autorizador não precisa manter nenhum estado; o próprio token é sulficiente para verificar a autorização de um portador de token.

Os JWTs são assinados usando um algoritmo de assinatura digital (por exemplo, RSA) que não pode ser forjado. Por isso, qualquer pessoa que confie no certificado do assinante pode confiar com segurança que o JWT é autêntico. Não há necessidade de um servidor consultar o servidor emissor de token para confirmar sua autenticidade.

fonte: https://jwt.io/introduction/

> A maneira mais fácil de instalar é usar o pip:
```shell
pip install Flask-JWT
```
> Exemplo de implementação para testes
```python
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run()
```

## SQL Server e pyodbc

Nessa implementação foi utilizado o pyodbc para manipulação da base de dados SQL Server através de store procedures.
O pyodbc é um módulo Python de código aberto que simplifica o acesso aos bancos de dados ODBC. Ele implementa a especificação DB API 2.0, mas possui ainda mais conveniência Pythonic.

Stored Procedure, que traduzido significa Procedimento Armazenado, é uma conjunto de comandos em SQL que podem ser executados de uma só vez, como em uma função. Ele armazena tarefas repetitivas e aceita parâmetros de entrada para que a tarefa seja efetuada de acordo com a necessidade individual. Nesse projeto foram desenvolvidos. As Stored Procedures implementadas nesse projeto são: 

- sp_Clientes_InsertValue
- sp_Clientes_GetValueById
- sp_Clientes_GetAllValues
- sp_Clientes_DeleteValue

> A maneira mais fácil de instalar é usar o pip:

```shell
pip install pyodbc
```
> Exemplo de implementação para testes
```python
import pyodbc

server = 'servidor'
database = 'base_de_dados'
username = 'user'
password = 'senhs'

#connection string utilizado para o sql server
db_connection = ('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  

# estabelecendo conexão
cnxn = pyodbc.connect(db_connection)
cursor = cnxn.cursor()

#Executando uma query exemplo que, obter a versão do banco de dados
cursor.execute("SELECT @@version;")

#imprimindo dados
row = cursor.fetchone()
while row:
    print (row[0])
    row = cursor.fetchone()
```

## Testes unitários (unittest e coverage)

Teste de unidade é toda a aplicação de teste nas assinaturas de entrada e saída de um sistema. Consiste em validar dados válidos e inválidos via I/O (entrada/saída) sendo aplicado por desenvolvedores ou analistas de teste. Uma unidade é a menor parte testável de um programa de computador. Em programação procedural, uma unidade pode ser uma função individual ou um procedimento. Idealmente, cada teste de unidade é independente dos demais, o que possibilita ao programador testar cada módulo isoladamente.
O framework `unittest` foi originalmente inspirada por JUnit e tem semelhante com os principais frameworks de teste de unitários de outras linguagens. Ele suporta automação de teste, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes da estrutura de relatório.
O `Coverage.py` é uma ferramenta para medir a cobertura de código de programas Python. Ele monitora seu programa, observando quais partes do código foram executadas e, em seguida, analisa a fonte para identificar o código que poderia ter sido executado, mas não foi. A medição da cobertura é normalmente usada para avaliar a eficácia dos testes. Ele pode mostrar quais partes do seu código estão sendo exercitadas por testes e quais não estão.

> A maneira mais fácil de instalar é usar o pip:
```shell
pip install coverage
```
> Exemplo de implementação para testes
```python
import unittest
import sys
sys.path.append("..//cadastro//resources//")
from user import User

class TestSum(unittest.TestCase):

    def test_sum(self):
        c =   User(1, 'fabio', 'senha_teste')
        self.assertEqual(c.username, "fabio", "Deveria ser Fabio")

if __name__ == '__main__':
    unittest.main()
```

> Para executar os teste navegue até a pasta tests e execute o comando abaixo:
```shell
coverage run -m unittest discover
coverage report
```

## Suporte

Por favor entre em contato conosco via [Email]