# Desafio

Usando [Django](https://www.djangoproject.com/) e [Django REST framework](https://www.django-rest-framework.org/) desenvolva uma API REST que permita usuários gerenciar empréstimos.

## Setup

Crie um arquivo .env na raiz do projeto com suas informações do SGBD Postgres, exemplo:

```dotenv
DB_NAME=onidata
DB_USER=postgres
DB_PASSWORD=senha
DB_HOST=localhost
```

Instale os requirements utilizando o comando:

```shell script
pip install -r requirements.txt
```

Teste para verificar se está tudo perfeito com o setup:

```shell script
python manage.py test
```

## Utilizando o sistema

Rode as migrações para criar as tabelas iniciais da api:

```shell script
python manage.py migrate
```

### Adicionando Dados Iniciais ao Sistema

Caso queria utilizar dados default para popular o banco de dados do sistema, existem fixtures para todos os apps.

#### Usuários

Para popular usuários no sistema, basta rodar o seguinte comando:

```shell script
python manage.py loaddata users
```

Com isso será criado um usuário administrador com password ```admin13``` e ```test1234``` para demais usuários.

Outras informações dos usuários cadastrados você pode encontrar no diretório ```fixtures``` dentro do app Users.

Você também pode cadastrar usuários com o comando:

```shell script
python manage.py create_user -u <username> -p <password> -e <email> -c <cpf>
```

#### Empréstimos

Para popular empréstimos no sistema, basta rodar o seguinte comando:

```shell script
python manage.py loaddata loans
```

As informações dos empréstimos cadastrados você pode encontrar em no diretório ```fixtures``` dentro do app Loans.

#### Pagamentos

Para popular pagamentos no sistema, basta rodar o seguinte comando:

```shell script
python manage.py loaddata payments
```

As informações dos pagamentos cadastrados você pode encontrar em no diretório ```fixtures``` dentro do app Payments.

### Criando um usuário administrador

Caso não tenha utilizado os dados iniciais do sistema pelo ```loaddata``` crie um usuário administrador para utilizar o sistema:

```shell script
python manage.py createsuperuser
```

### Autenticação

Para acessar o seu token e utilizar todas as rotas do sistema, basta acessar:

```
GET /api-token-auth/
```

Passando as informações de username e password

```json
{
    "username": "username",
    "password": "password"
}
```

### Usuários

Para gerenciar usuários no sistema as rotas utilizadas são:

```
GET /api/users
POST /api/users
GET /api/users/:id
PUT /api/users/:id
DELETE /api/users/:id
```

### Empréstimos

Para gerenciar os empréstimos no sistema as rotas utilizadas são:

```
GET /api/loans
POST /api/loans
GET /api/loans/:id
PUT /api/loans/:id
DELETE /api/loans/:id
```

### Pagamentos

Para gerenciar os pagamentos no sistema as rotas utilizadas são:

```
GET /api/payments
POST /api/payments
GET /api/payments/:id
PUT /api/payments/:id
DELETE /api/payments/:id
```

## Critérios de aceite
* Usuários devem ser capazes de inserir empréstimos e seus respectivos pagamentos
* Usuários devem ser capazer de visualizar seus empréstimos e pagamentos
* Usuários devem ser capazes de visualizar o [saldo devedor](https://duckduckgo.com/?q=saldo+devedor) de cada um dos seus empréstimos
    * Você pode decidir onde e como mostrar a informação
    * O saldo devedor nada mais é do que o quanto o cliente ainda deve para o banco
    * O saldo devedor deve considerar a taxa de juros do empréstimo e descontar o que já foi pago
* Usuários não podem ver ou editar empréstimos ou pagamentos de outros usuários
* A autenticação da API deve ser feita via token
    * Não é necessário desenvolver endpoints para criação/gerenciamento de usuários
* Os empréstimos devem conter no mínimo as informações abaixo:
    * Identificador - um identificador aleatório gerado automaticamente
    * Valor nominal - o valor emprestado pelo banco
    * Taxa de juros - a taxa de juros mensal do empréstimo
    * Endereço de IP - endereço de IP que cadastrou o empréstimo
    * Data de solicitação - a data em que o empréstimo foi solicitado
    * Banco - informações do banco que emprestou o dinheiro (pode ser um simples campo de texto)
    * Cliente - informações do cliente que pegou o empréstimo (pode ser um simples campo de texto)
* Os pagamentos devem conter no mínimo as informações abaixo:
    * Identificador do empréstimo
    * Data do pagamento
    * Valor do pagamento
* Testes
    * As funcionalidade principais devem estar com [testes](https://docs.djangoproject.com/en/3.1/topics/testing/) escritos
    * Você pode decidir quais os testes que mais agregam valor ao projeto

## Extra (opcional)
* Cálculo do saldo devedor usando [juros compostos](https://duckduckgo.com/?q=juros+compostos) [pro rata dia](https://duckduckgo.com/?q=pro+rata+dia).
* Expandir o modelo financeiro adicionando [IOF](https://duckduckgo.com/?q=imposto+sobre+operações+financeiras+operação+de+crédito), seguro, etc...

## Informações adicionais
Você pode organizar a API e o banco de dados da maneira que achar que faz mais sentido. Além disso, sinta-se a vontade para adicionar ferramentas ou funcionalidades que ache relevante.

## O que vamos avaliar
1. O cumprimento dos requisitos obrigatórios
2. A forma que o código está organizado
3. O domínio das funcionalidade do Django e DRF
4. A abordagem e abrangência dos testes do código
5. A simplicidade da solução
6. Aderência a [PEP 8](https://duckduckgo.com/?q=pep8)
7. A implementação de requisitos opcionais
8. A implementação de funcionalidades extras
