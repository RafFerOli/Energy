# Projeto: Avaliação de Eficiência Energética Para Construções (Energy_App)

Este projeto é um sistema de predição de valores de cargas de aquecimento e resfriamento geradas em edificações diversas para classificação de eficiência energética para analise de dados. O sistema é composto por 2 componentes básicos que se comunicam utilizando REST. 

## Estrutura da API

**Energy_app_api:**

A API é construída em Python, utilizando o framework Flask para criar endpoints robustos e escaláveis para interagirem com a tabela "Energy" que se encontra em um banco de dados "SQlite". O sistema utiliza o framework "SQLAlchemy" para trabalhar com as informações principais e conta com a documentação em "Swagger".

**Energy_app_front:**

A interface de operação do usuário é construída em HTML, CSS e JavaScript. Nela o usuário tem a possibilidade de castrado de dados do cliente, visualização de informações principais, alteração de dados, pesquisa, busca de localização através das informações cadastradas e busca de dados para cadastro através do C.N.P.J.

## Tecnologias Utilizadas

   **Python:** Linguagem de programação utilizada para o desenvolvimento da API.
   
   **HTML:** Linguagem de programação utilizada para o desenvolvimento da interface.
   
   **CSS:** Linguagem de programação utilizada para o desenvolvimento da interface.
   
   **Javascript:** Linguagem de programação utilizada para o desenvolvimento da da interface.
   
   **Flask:** Framework web leve e flexível para criar endpoints RESTful.
   
   **SQLAlchemy:** Framework para interagir com o banco de dados SQL de forma simplificada.
   
   **SQLite:** Banco de dados embutido para armazenamento de dados de forma eficiente e confiável.
