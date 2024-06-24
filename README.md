# Infraestrutura e Servicos Web
Projeto Final: Aplicação Web Simples com Contêineres e Ansible

## Descrição
O projeto implementa login e cadastro de usuários pelo navegador web.

## Estrutura 
O projeto está dividido em três containers Docker, banco de dados, front-end e back-end. Ao realizar um novo registro ou efetuar login, os dados de usuário e senha são enviados por meio da API REST para o back-end que realiza a inserção/validação no banco de dados e retorna ao front-end a resposta de confirmação.
O deploy é realizado pelo Ansible.

### Tecnologias:
Front-end: HTML, CSS e PHP

Back-end: Python

Banco de dados: PostgreSQL


## Como executar:
Execute o arquivo playbook.yml
"sudo ansible-playbook playbook.yml"

Acesse, pelo navegador, a url: "http://192.168.15.4:8000"
