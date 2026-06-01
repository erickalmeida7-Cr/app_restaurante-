import streamlit as st
import pandas as pd

def listar_produtos():
    st.header("📋 Cardápio Atual")
    # Lê os dados que foram inicializados de forma segura no main.py
    if not st.session_state.cardapio:
        st.warning("O cardápio está vazio.")
    else:
        df_cardapio = pd.DataFrame(st.session_state.cardapio)
        df_cardapio.columns = ["Código", "Nome do Produto", "Preço (R$)"]
        st.dataframe(df_cardapio.set_index("Código"), use_container_width=True)

def cadastrar_produto():
    st.header("✨ Cadastrar Novo Produto")
    
    with st.form("form_cadastro", clear_on_submit=True):
        novo_codigo = st.number_input("Código do Produto:", min_value=1, step=1)
        novo_nome = st.text_input("Nome do Produto:")
        novo_preco = st.number_input("Preço (R$):", min_value=0.1, step=0.5, format="%.2f")
        
        botao_cadastrar = st.form_submit_button("Salvar Produto")
        
        if botao_cadastrar:
            codigo_existe = any(p["codigo"] == novo_codigo for p in st.session_state.cardapio)
            
            if codigo_existe:
                st.error("❌ Erro: Já existe um produto com este código.")
            elif not novo_nome.strip():
                st.error("❌ Erro: O nome do produto não pode ficar em branco.")
            else:
                st.session_state.cardapio.append({
                    "codigo": novo_codigo,
                    "nome": novo_nome.strip(),
                    "preco": novo_preco
                })
                st.success(f"✔️ Produto '{novo_nome}' cadastrado com sucesso!")
