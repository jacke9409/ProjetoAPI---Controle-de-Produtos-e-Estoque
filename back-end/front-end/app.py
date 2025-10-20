# front-end
import streamlit as st
import requests 
# • Consumir a API via aplicativo Streamlit (front-end).
# • Garantir tratamento de erros, validação e
# documentação da API.
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de produtos", page_icon="🛒")

st.title("🛍 Gerenciador de produtos")

#Menu lateral sidebar
#Menu lateral sidebar
menu = st.sidebar.radio("Navegação", ["Produto", "Adicionar produto", "Atualizar produto", "Deletar produto"])
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Jackelyne")
st.sidebar.markdown("2025")

if menu == "Produto":
    st.subheader("Lista de produtos")
    try:
        response = requests.get(f"{API_URL}/produtos/", timeout=5)
        response.raise_for_status()
        produtos = response.json().get("produtos", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao conectar com a API: {e}")
        produtos = []

    if produtos:
        for produto in produtos:
            st.write(f" **ID:** {produto['id']}  \n **Nome:** {produto['name']}  \n **Preço:** R$ {produto['price']}  \n **Quantidade:** {produto['quantity']}")
    else:
        st.info("Nenhum produto encontrado.")