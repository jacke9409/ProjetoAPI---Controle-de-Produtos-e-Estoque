
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
    st.subheader("Catálogo de produtos")
    response = requests.get(f"{API_URL}/produtos/")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto encontrado.")

elif menu == "Adicionar produto":
    st.subheader("Adicionar novo produto")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade em estoque", min_value=0, step=1)

    if st.button("Adicionar produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos/", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto.")


elif menu == "Atualizar produto":
    st.subheader("Atualizar produto existente")
    id = st.text_input("ID do produto a ser atualizado")
    preco = st.number_input("Novo preço do produto", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Nova quantidade em estoque", min_value=0, step=1)

    if st.button("Atualizar produto"):
        id_produto= st.number_input("ID do produto a ser atualizado", min_value=0, step=1)
        preco = st.number_input("Novo preço do produto", min_value=0.0, format="%.2f")
        quantidade = st.number_input("Nova quantidade em estoque", min_value=0, step=1)
    
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params={"preco": preco, "quantidade": quantidade}
        )
        if response.status_code == 200:
            st.success("Produto atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar o produto.")

elif menu == "Deletar produto":
    st.subheader("Deletar produto")
    id_produto= st.number_input("ID do produto a ser deletado", min_value=0, step=1)

    if st.button("Deletar produto"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")
        if response.status_code == 200:
            st.success("Produto deletado com sucesso!")
        else:
            st.error("Erro ao deletar o produto.")
            