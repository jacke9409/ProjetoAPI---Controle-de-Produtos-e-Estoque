from fastapi import FastAPI
from funcoes import listar_produtos, cadastrar_produto, atualizar_produto, excluir_produto

app = FastAPI(title="API de Gerenciamento de Produtos")
@app.get("/produtos/")
def home():
    return {"mensagem": "Bem-vinda(o) a API de Gerenciamento de Produtos!"}

@app.get("/produtos/")
def obter_produtos():
    produtos = listar_produtos()
    lista_produtos = []
    for produto in produtos:
        lista_produtos.append({
            "id": produto[0],
            "nome": produto[1],
            "preco": float(produto[2]),
            "quantidade": produto[3]
        })
    return {"produtos": lista_produtos}  
   
app.post("/produtos/")
def adicionar_produto(nome: str, preco: float, quantidade: int):
    cadastrar_produto(nome, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

app.put("/produtos/")
def atualizar_produto(nome: str, preco: float, quantidade: int):
    atualizar_produto(nome, preco, quantidade)
    return {"mensagem": "Produto atualizado com sucesso!"}
