import streamlit as st

def realizar_pedido():
    st.header("🛒 Novo Pedido")
    
    if not st.session_state.cardapio:
        st.error("Não há produtos no cardápio para realizar um pedido.")
        return

    opcoes_produtos = {f"{p['nome']} (R$ {p['preco']:.2f})": p for p in st.session_state.cardapio}
    produto_selecionado_texto = st.selectbox("Selecione o Produto:", list(opcoes_produtos.keys()))
    quantidade = st.number_input("Quantidade:", min_value=1, step=1)
    
    if st.button("Adicionar ao Carrinho"):
        produto_real = opcoes_produtos[produto_selecionado_texto]
        st.session_state.carrinho_atual.append({
            "produto": produto_real,
            "quantidade": quantidade
        })
        st.toast(f"{quantidade}x {produto_real['nome']} adicionado!")

    if st.session_state.carrinho_atual:
        st.write("### Carrinho Atual")
        total_pedido = 0
        
        for item in st.session_state.carrinho_atual:
            subtotal = item["produto"]["preco"] * item["quantidade"]
            total_pedido += subtotal
            st.write(f"- {item['quantidade']}x **{item['produto']['nome']}** — R$ {subtotal:.2f}")
        
        st.write(f"#### **Total: R$ {total_pedido:.2f}**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏁 Finalizar Pedido", type="primary"):
                novo_pedido = {
                    "id": len(st.session_state.historico_pedidos) + 1,
                    "itens": list(st.session_state.carrinho_atual),
                    "total": total_pedido
                }
                st.session_state.historico_pedidos.append(novo_pedido)
                st.session_state.carrinho_atual = []
                st.success("🎉 Pedido registrado com sucesso!")
                st.rerun()
        with col2:
            if st.button("🗑️ Limpar Carrinho"):
                st.session_state.carrinho_atual = []
                st.warning("Carrinho esvaziado.")
                st.rerun()

def exibir_relatorios():
    st.header("📊 Relatório Geral do Sistema")
    
    total_vendas = len(st.session_state.historico_pedidos)
    
    if total_vendas == 0:
        st.info("Nenhum pedido foi realizado hoje.")
        return

    faturamento_total = sum(p["total"] for p in st.session_state.historico_pedidos)
    
    contagem_produtos = {}
    for pedido in st.session_state.historico_pedidos:
        for item in pedido["itens"]:
            nome_prod = item["produto"]["nome"]
            contagem_produtos[nome_prod] = contagem_produtos.get(nome_prod, 0) + item["quantidade"]
    
    prod_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    qtd_mais_vendido = contagem_produtos[prod_mais_vendido]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Pedidos", total_vendas)
    col2.metric("Faturamento Total", f"R$ {faturamento_total:.2f}")
    col3.metric("Mais Vendido", prod_mais_vendido, f"{qtd_mais_vendido} un.")
    
    st.write("### 📝 Histórico de Pedidos Realizados")
    for p in st.session_state.historico_pedidos:
        with st.expander(f"Pedido #{p['id']} — Total: R$ {p['total']:.2f}"):
            for item in p["itens"]:
                st.write(f"• {item['quantidade']}x {item['produto']['nome']} (R$ {item['produto']['preco']:.2f} cada)")
