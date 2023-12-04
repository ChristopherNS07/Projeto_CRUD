import classeConexaoBD as conexao

if __name__ == "__main__":
    conexao = conexao.ConexaoBanco(host="localhost", user="root", password="", database="clinimed")

conexao.conectar()