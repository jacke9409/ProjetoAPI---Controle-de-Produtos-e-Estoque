from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    nome SERIAL PRIMARY KEY,
                    preco FLOAT NOT NULL,
                    quantidade INT NOT NULL
                    )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()


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

# criando funcao listar produtos
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "SELECT * FROM produtos"
    cursor.execute(comando)
    resultados = cursor.fetchall()
    cursor.close()