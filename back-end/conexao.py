import psycopg2
from dotenv import load_dotenv
import os
# carregar variáveis de ambiente do arquivo .env
load_dotenv()
params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
    }
def conectar():
    """Estabelece uma conexão com o banco de dados PostgreSQL."""
    try:
        conexao = psycopg2.connect(**params)
        cursor = conexao.cursor()
        print("Conexão bem-sucedida")
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão: {erro}")
        return None, None
