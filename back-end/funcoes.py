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
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, preco, quantidade)
                VALUES (%s, %s, %s)
                """, (nome, preco, quantidade))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
# aqui eu criei a função cadastrar produto
# corrigi erro de criar

# criando funcao listar produtos
def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            return produtos
        except Exception as erro:
            print(f"Erro ao listar os produtos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()



def atualizar_produto(nome, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                UPDATE produtos
                SET preco = %s, quantidade = %s
                WHERE nome = %s
                """, (preco, quantidade, nome))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def excluir_produto(nome):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                DELETE FROM produtos
                WHERE nome = %s
                """, (nome,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao excluir o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()