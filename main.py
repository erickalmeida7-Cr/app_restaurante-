import sys
import os
import streamlit as st

# Sistema de caminhos absolutos para servidores Linux (Streamlit Cloud)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuração da página web
st.set_page_config(page_title="Gestão de Restaurante", page_icon="🍔", layout="centered")

# --- INICIALIZAÇÃO DOS DADOS NA SESSÃO GLOBAL ---
# Ao colocar aqui, o Streamlit cria o estado antes de qualquer importação secundária
if "cardapio" not in st.session_state:
    st.session_state.cardapio = [
        {"codigo": 1, "nome": "Hambúrguer Artesanal", "preco": 28.50},
        {"codigo": 2, "nome": "Batata Frita Média", "preco": 12.00},
        {"codigo": 3, "nome": "Refrigerante Lata", "preco": 6.00},
    ]

if "historico_pedidos" not in st.session_state:
    st.session_state.historico_pedidos = []

if "carrinho_atual" not in st.session_state:
    st.session_state.carrinho_atual = []

# Agora os submódulos podem ser importados com segurança
import produtos
import pedidos

st.title("🍔PODRÃO DO ERICK")
st.caption("Aqui a sua satisfação é garantida")
st.write("---")

opcao = st.sidebar.radio(
    "Navegue pelo Sistema:",
    [
        "1. Ver Cardápio / Listar Produtos", 
        "2. Cadastrar Produto", 
        "3. Realizar Pedido", 
        "4. Relatórios de Vendas"
    ]
)

if opcao == "1. Ver Cardápio / Listar Produtos":
    produtos.listar_produtos()

elif opcao == "2. Cadastrar Produto":
    produtos.cadastrar_produto()

elif opcao == "3. Realizar Pedido":
    pedidos.realizar_pedido()

elif opcao == "4. Relatórios de Vendas":
    pedidos.exibir_relatorios()
