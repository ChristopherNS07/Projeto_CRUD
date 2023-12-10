import os
import time
from tabulate import tabulate
from IPython.core.display_functions import display
class PacienteDAO:
    def __init__(self, conexao):
        self.conexao = conexao


    def cadastrar_paciente(self, paciente):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO TB_PACIENTE (CPF_PACIENTE, RG_PACIENTE, NOME_PACIENTE, ENDERECO_PACIENTE, "\
                  "CEP_PACIENTE, CELULAR_PACIENTE, DTNASC_PACIENTE, SEXO_PACIENTE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

            valores = (paciente.cpf_paciente, paciente.rg_paciente, paciente.nome_paciente, paciente.endereco_paciente,
                       paciente.cep_paciente, paciente.celular_paciente, paciente.dt_nascimento_paciente, paciente.sexo_paciente)

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()

            os.system("cls")
            print("Paciente cadastrado com Sucesso!")
            time.sleep(3)

        except Exception as e:
            print("Erro: ", e)

    def consultar_paciente(self, cpf_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = ("SELECT CPF_PACIENTE, RG_PACIENTE, NOME_PACIENTE, ENDERECO_PACIENTE, CEP_PACIENTE, CELULAR_PACIENTE, " \
               "DTNASC_PACIENTE, SEXO_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s")

        try:
            cursor.execute(sql, (cpf_procurado,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system("cls")
                print("Paciente não encontrado")
                time.sleep(3)

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result) # append() usado para acrescentar um elemento no final da lista

                colunas = ['CPF', 'RG', 'NOME', 'ENDERECO', 'CEP', 'CELULAR', 'DT_NASCIMENTO', 'SEXO']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
                display(tabela)
                input("\nPressione uma tecla para continuar...")

        except Exception as e:
            print("Erro: ", e)

    def consultar_todos_pacientes(self):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CPF_PACIENTE, RG_PACIENTE, NOME_PACIENTE, ENDERECO_PACIENTE, CEP_PACIENTE, CELULAR_PACIENTE, " \
               "DTNASC_PACIENTE, SEXO_PACIENTE FROM TB_PACIENTE"

        try:
            cursor.execute(sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system("cls")
                print("Não possui cadastros!")

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result)

                colunas = ['CPF', 'RG', 'NOME', 'ENDERECO', 'CEP', 'CELULAR', 'DT_NASCIMENTO', 'SEXO']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid', )
                display(tabela)
                input("\nPressione uma tecla para continuar...")

        except Exception as e:
            print("Erro: ", e)

    def excluir_pacientes(self, cpf_procurado_paciente):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CPF_PACIENTE, RG_PACIENTE, NOME_PACIENTE, ENDERECO_PACIENTE, CEP_PACIENTE, CELULAR_PACIENTE, " \
               "DTNASC_PACIENTE, SEXO_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"

        try:
            cursor.execute(sql, (cpf_procurado_paciente,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system("cls")
                print("Paciente não cadastrado!")
                time.sleep(3)

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result)

                colunas = ['CPF', 'RG', 'NOME', 'ENDERECO', 'CEP', 'CELULAR', 'DT_NASCIMENTO', 'SEXO']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
                display(tabela)
                exclusao = input("\nTem certeza que deseja excluir esse cadastro ?\n\nS - Sim ou N - Não: ")

                if exclusao.upper() == "S":
                    cursor = self.conexao.conexao.cursor()
                    sql = "DELETE FROM tb_paciente WHERE CPF_PACIENTE = %s"

                    cursor.execute(sql, (cpf_procurado_paciente,))
                    self.conexao.conexao.commit()

                    os.system("cls")
                    print("Cadastro Excluido com Sucesso!")
                    time.sleep(2)
                    input("Pressione uma tecla para continuar...")
                elif exclusao.upper() == "N":
                    print("Retornando ao menu principal...")
                    time.sleep(2)
                else:
                    print("Digito inválido!\nRetornando ao menu principal...")
                    time.sleep(2)

        except Exception as e:
            print("Erro: ", e)

    def editar_paciente(self, cpf_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CPF_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"
        cursor.execute(sql, (cpf_procurado,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            os.system("cls")
            print("Registro não encontrado!")
            time.sleep(3)

        else:

            cpf_paciente = input("Novo CPF: ")
            cursor.execute(sql, (cpf_paciente,))
            resultado = cursor.fetchall()

            if len(resultado) != 0 and cpf_paciente != cpf_procurado:
                os.system("cls")
                print("CPF já cadastrado para outro paciente.")
                time.sleep(3)

            else:
                rg_paciente = input("Novo RG: ")

                sql = "SELECT RG_PACIENTE FROM TB_PACIENTE WHERE RG_PACIENTE = %s"
                sql2 = "SELECT RG_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"

                cursor.execute(sql, (rg_paciente,))
                resultado = cursor.fetchall()

                cursor.execute(sql2, (cpf_procurado,))
                resultado2 = cursor.fetchall()

                if (len(resultado) != 0 and ((rg_paciente,) in resultado2)) or len(resultado) == 0:
                    nome_paciente = input("Nome: ")
                    endereco_paciente = input("Endereço: ")
                    cep_paciente = input("CEP: ")
                    celular_paciente = input("Celular: ")
                    dt_nasc_paciente = input("Dt Nascimento (YYYY-MM-DD):")
                    sexo_paciente = None

                    while sexo_paciente != 'M' and sexo_paciente != 'F':
                        sexo_paciente = input("Sexo (M ou F): ")
                        sexo_paciente = sexo_paciente.upper()

                        if sexo_paciente != 'M' and sexo_paciente != 'F':
                            os.system('cls')
                            print("Sexo inválido!")
                            time.sleep(3)
                            os.system('cls')

                    sql = "UPDATE TB_PACIENTE SET CPF_PACIENTE = %s, RG_PACIENTE = %s, NOME_PACIENTE = %s, " \
                          "ENDERECO_PACIENTE = %s, CEP_PACIENTE = %s, CELULAR_PACIENTE = %s, DTNASC_PACIENTE = %s, " \
                          "SEXO_PACIENTE = %s WHERE CPF_PACIENTE = %s"

                    valores = (cpf_paciente, rg_paciente, nome_paciente, endereco_paciente, cep_paciente,
                               celular_paciente, dt_nasc_paciente, sexo_paciente, cpf_procurado)

                    try:
                        cursor.execute(sql, valores)
                        self.conexao.conexao.commit()
                        os.system("cls")
                        print(cursor.rowcount, "registro alterado.")
                        time.sleep(3)

                    except Exception as e:
                        print("Erro: ", e)

                else:
                    os.system("cls")
                    print("RG já cadastrado para outro paciente!")
                    time.sleep(3)

