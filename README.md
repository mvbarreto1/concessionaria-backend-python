Sistema de Concessionária (Python + PostgreSQL)

Este projeto consiste em um sistema de gerenciamento de concessionária desenvolvido em Python, com persistência de dados em PostgreSQL e execução via linha de comando (CLI). O sistema simula operações comuns de uma concessionária, como cadastro de funcionários, registro de vendas, cálculo de comissões e geração de relatórios gerenciais.

O projeto foi desenvolvido como parte de um portfólio técnico, com foco em fundamentos de backend, integração entre Python e banco de dados relacional, uso de SQL para consultas analíticas e aplicação de regras de negócio de forma clara e organizada, sem utilização de frameworks.

Objetivo do Projeto

O objetivo principal é demonstrar a capacidade de projetar e implementar um sistema funcional que integre lógica de negócio, persistência de dados e geração de relatórios, simulando um cenário real de uso. O sistema foi pensado para operar de forma simples via terminal, priorizando clareza do código, consistência dos dados e organização da arquitetura.

Tecnologias Utilizadas

Python

PostgreSQL

SQL

Execução via terminal (CLI)

Funcionalidades

O sistema permite o cadastro e a listagem de funcionários, que são utilizados como referência para o registro das vendas. Cada venda é associada a um funcionário responsável, garantindo rastreabilidade das operações.

A partir do registro das vendas, o sistema realiza automaticamente o cálculo de comissões com base em regras definidas, armazenando essas informações no banco de dados. Além disso, são disponibilizados relatórios que permitem analisar o desempenho de vendas e o valor de comissões por funcionário.

O sistema também oferece a exportação de relatórios de vendas em formato JSON, simulando uma integração com outros sistemas ou a geração de arquivos para consumo externo.

Durante toda a operação, são aplicadas validações de dados de entrada para garantir consistência e evitar registros inválidos.

Arquitetura e Organização

A arquitetura do projeto foi pensada para manter uma separação clara de responsabilidades. O Python é responsável pela interação com o usuário via terminal, validação de dados e execução das consultas SQL. O PostgreSQL é utilizado como camada de persistência, armazenando funcionários, vendas e comissões, além de ser a base para a geração dos relatórios.

As regras de negócio são implementadas de forma explícita, evitando soluções artificiais ou dependentes de frameworks, o que reforça o entendimento dos fundamentos de backend e banco de dados relacional.

Estrutura do Projeto
/
├── main.py              # Arquivo principal com o menu e o fluxo do sistema
├── database.py          # Configuração e conexão com o banco de dados
├── queries.sql          # Consultas SQL utilizadas pelo sistema
├── relatorios.py        # Funções responsáveis pelos relatórios
├── export_json.py       # Exportação de relatórios em formato JSON
└── README.md

A estrutura pode variar conforme a versão do projeto.

Execução do Projeto

Para executar o projeto, é necessário criar previamente um banco de dados no PostgreSQL e executar o script SQL responsável pela criação das tabelas. Em seguida, deve-se configurar a conexão com o banco de dados no arquivo database.py.

Com o ambiente configurado, o sistema pode ser iniciado via terminal com o comando:

python main.py

A partir do menu interativo, o usuário pode cadastrar funcionários, registrar vendas, consultar relatórios e exportar dados.

Considerações Finais

Este projeto foi desenvolvido com foco em aprendizado prático e qualidade técnica, simulando demandas comuns de sistemas internos utilizados por empresas. Ele demonstra integração entre Python e PostgreSQL, uso consciente de SQL e aplicação de regras de negócio de forma estruturada, sendo adequado como case de backend e análise de dados para portfólio profissional.

Desenvolvido por Marcus Viniccius Araujo Barreto

