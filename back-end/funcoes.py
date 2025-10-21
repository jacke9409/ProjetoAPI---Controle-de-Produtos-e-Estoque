from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco DECIMAL(10,2),
                    quantidade INT
                    )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()


def cadastrar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade)
                VALUES (%s, %s, %s, %s)
                """, (nome, categoria, preco, quantidade))
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


def atualizar_produto(id_produto, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                UPDATE produtos
                SET preco = %s, quantidade = %s
                WHERE id_produto = %s
            """, (preco, quantidade, id_produto))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def excluir_produto(id_produto):  # <--- está usando nome, não id_produto

    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute( "DELETE FROM produtos WHERE id=%s", 
                (id_produto,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao excluir o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

