# Sistema de Gestão de Pedidos para Restaurante

Este projeto consiste num sistema modular de gestão de pedidos, cardápio e relatórios comerciais para restaurantes. Projeto desenvolvido em Python, a aplicação é dividida em módulos independentes com uma interface web interativa fornecida pelo Streamlit.

## Estrutura do Projeto

O sistema foi componentizado em quatro arquivos principais, isolando as responsabilidades de interface, lógica de negócio e persistência de dados:

* **`main.py`**: Ponto de entrada do sistema. Gerencia o menu de navegação e o fluxo principal da aplicação.
* **`produtos.py`**: Concentra a lógica do Módulo de Cadastro e Listagem de Produtos (Cardápio).
* **`pedidos.py`**: Contém as rotinas para abertura de novos pedidos (carrinho de compras) e a geração dos relatórios estatísticos.
* **`dados.py`**: Módulo central de persistência. Inicializa e gerencia os estados de dados usando o `st.session_state` para reter as informações durante o ciclo de vida da aplicação.

## Tecnologias Utilizadas

* **Python 3.x** (Lógica principal, dicionários e listas)
* **Streamlit** (Camada de visualização de dados e interface do utilizador)
* **Pandas** (Estruturação e exibição tabular do cardápio)

## Links
* **Link do Github**: [https://github.com/erickalmeida7-Cr/app_restaurante-]
* **Aplicação em Nuvem**: https://c5tr5mbvvkvxxoicixtpvr.streamlit.app/
