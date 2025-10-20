from fastapi import FastAPI
import funcoes

app = FastAPI(title="API de Gerenciamento de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Gerenciamento de Produtos"}

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcoes.cadastrar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso"}

@app.get("/produtos")
def catalogo():
    produtos = funcoes.listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {"produtos": lista}

@app.put("/produtos/{id_produtos}")
def atualizar_produto(id_produto: int, preco: float, quantidade: int):
    produto = funcoes.buscar_estoque(id_produto)
    if produto:
        funcoes.atualizar_produto(produto, preco, quantidade)
        return {"mensagem": "Produto atualizado com sucesso"}
    else:
        return {"mensagem": "Produto não encontrado"}

@app.delete("/produtos")
def deletar_produto(id_produto):
    deletar = funcoes.excluir_produto(id_produto)
    if deletar:
        return {"mensagem": "Produto excluído com sucesso"}
    else:
        return {"mensagem": "Produto não encontrado"}
