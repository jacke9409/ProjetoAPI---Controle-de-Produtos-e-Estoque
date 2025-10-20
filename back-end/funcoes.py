from conexao import conectar

def cadastrar_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)"
    valores = (nome, preco, quantidade)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
# aqui eu criei a função cadastrar produto