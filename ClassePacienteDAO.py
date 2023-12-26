import os
import time
from tabulate import tabulate
from IPython.core.display_functions import display
import pandas as pd
from tkinter import filedialog
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

                op_csv = int(input("\nDeseja exportar um relatório em CSV?\n1 - Sim ou 2 - Não\n\nEscolha uma opção: "))

                if op_csv == 1:
                    df = pd.DataFrame(resultados[1:], columns=resultados[0])
                    caminho = filedialog.askdirectory(title="Escolha o diretório")

                    if caminho:
                        nome_arquivo = input("\nDigite um nome para o arquivo: ")
                        df.to_csv((caminho + '/' + nome_arquivo + '.csv'), index=False, encoding='utf-8-sig')

                        print("Tabela Exportada!")

                    else:
                        print("Operação cancelada pelo usuário.")

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
                    print("Cadastro excluido com sucesso!")
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

    # def editar_paciente(self, cpf_procurado):
    #     cursor = self.conexao.conexao.cursor()
    #     sql = "SELECT CPF_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"
    #     cursor.execute(sql, (cpf_procurado,))
    #     resultado = cursor.fetchall()
    #
    #     if len(resultado) == 0:
    #         os.system('cls')
    #         print("Paciente não encontrado!")
    #         time.sleep(3)
    #
    #     else:
    #         sql = '''SELECT NOME_PACIENTE, CPF_PACIENTE, RG_PACIENTE, ENDERECO_PACIENTE, CEP_PACIENTE,
    #         CELULAR_PACIENTE, DTNASC_PACIENTE, SEXO_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s'''
    #         cursor.execute(sql, (cpf_procurado,))
    #         resultado = cursor.fetchall()
    #
    #         resultados = []
    #
    #         for result in resultado:
    #             result = list(result)
    #             resultados.append(result)
    #
    #         colunas = ['NOME', 'CPF', 'RG', 'ENDEREÇO', 'CEP', 'CELULAR', 'DATA DE NASCIMENTO', 'SEXO']
    #         tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
    #         display(tabela)
    #
    #         op_decisao = int(input("\nDeseja alterar o cadastro desse paciente ?\n1. Sim\n2. Não\n Digite uma das opções: "))
    #
    #         if op_decisao == 1:
    #             opcao = int(input("Opções disponiveis: \n1 - NOME\n2 - CPF\n3 - RG\n4 - ENDEREÇO\n5 - CEP\n6 - CELULAR"
    #                               "\n7 - DATA DE NASCIMENTO\n8 - SEXO\n9 - SAIR\n Escolha uma das opções: "))
    #
    #             if opcao == 1:
    #                 try:
    #                     novo_nome = input("\nNovo nome: ")
    #                     sql = "UPDATE TB_PACIENTE SET NOME_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                     valores = (novo_nome, cpf_procurado,)
    #                     cursor.execute(sql, valores)
    #                     self.conexao.conexao.commit()
    #
    #                     input("\nNome alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 2:
    #                 try:
    #                     novo_cpf = input("Digite o novo CPF: ")
    #                     sql = "SELECT CPF_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"
    #                     cursor.execute(sql, (novo_cpf,))
    #                     resultado = cursor.fetchall()
    #
    #                     if len(resultado) != 0 and novo_cpf != cpf_procurado:
    #                         os.system('cls')
    #                         print("CPF já cadastrado em outro paciente.")
    #                         time.sleep(3)
    #
    #                     elif len(resultado) != 0 and novo_cpf == cpf_procurado:
    #                         os.system('cls')
    #                         print("CPF digitado igual ao CPF procurado.")
    #                         time.sleep(3)
    #
    #                     else:
    #
    #                         sql = "UPDATE TB_PACIENTE SET CPF_PACIENTE = %s WHERE CPF_PACIENTE = %s "
    #                         valores = (novo_cpf, cpf_procurado,)
    #                         cursor.execute(sql, valores)
    #                         self.conexao.conexao.commit()
    #
    #                         input("\nCPF alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 3:
    #                 try:
    #                     novo_rg = input("Digite o novo RG: ")
    #                     sql = "SELECT RG_PACIENTE FROM TB_PACIENTE WHERE RG_PACIENTE = %s"
    #                     cursor.execute(sql, (novo_rg,))
    #                     resultado = cursor.fetchall()
    #
    #                     if len(resultado) != 0 and ((novo_rg,) in resultado):
    #                         os.system('cls')
    #                         print("RG já cadastrado em outro paciente.")
    #                         time.sleep(3)
    #
    #                     else:
    #
    #                         sql = "UPDATE TB_PACIENTE SET RG_PACIENTE = %s WHERE CPF_PACIENTE = %s "
    #                         valores = (novo_rg, cpf_procurado,)
    #                         cursor.execute(sql, valores)
    #                         self.conexao.conexao.commit()
    #
    #                         input("\nRG alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 4:
    #                 try:
    #                     endereco_novo = input("\nNovo Endereço: ")
    #                     sql = "UPDATE TB_PACIENTE SET ENDERECO_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                     valores = (endereco_novo, cpf_procurado,)
    #                     cursor.execute(sql, valores)
    #                     self.conexao.conexao.commit()
    #
    #                     input("\nEndereço alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 5:
    #                 try:
    #                     cep_novo = input("\nNovo CEP: ")
    #                     sql = "UPDATE TB_PACIENTE SET CEP_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                     valores = (cep_novo, cpf_procurado,)
    #                     cursor.execute(sql, valores)
    #                     self.conexao.conexao.commit()
    #
    #                     input("\nCEP alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 6:
    #                 try:
    #                     celular_novo = input("\nNovo Celular: ")
    #                     sql = "UPDATE TB_PACIENTE SET CELULAR_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                     valores = (celular_novo, cpf_procurado,)
    #                     cursor.execute(sql, valores)
    #                     self.conexao.conexao.commit()
    #
    #                     input("\nCelular alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 7:
    #                 try:
    #                     dtnasc_novo = input("\nNova Data de Nascimento (YYYY-mm-dd): ")
    #                     sql = "UPDATE TB_PACIENTE SET CELULAR_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                     valores = (dtnasc_novo, cpf_procurado,)
    #                     cursor.execute(sql, valores)
    #                     self.conexao.conexao.commit()
    #
    #                     input("\nData de nascimento alterado com sucesso!\n"
    #                           "Pressione uma tecla para voltar ao menu principal...\n")
    #
    #                 except Exception as e:
    #                     os.system('cls')
    #                     print(f"Erro: {e}")
    #
    #             elif opcao == 8:
    #                 while True:
    #                     try:
    #                         sexo_novo = input("\nNovo Sexo ('M' ou 'F'): ")
    #                         sexo_novo = sexo_novo.upper()
    #                         if sexo_novo != 'M' and sexo_novo != 'F':
    #                             os.system('cls')
    #                             print("\nDigito inválido, digite somente 'M' ou 'F'.")
    #                             time.sleep(0.5)
    #                         else:
    #                             sql = "UPDATE TB_PACIENTE SET SEXO_PACIENTE = %s WHERE CPF_PACIENTE = %s"
    #                             valores = (sexo_novo, cpf_procurado,)
    #                             cursor.execute(sql, valores)
    #                             self.conexao.conexao.commit()
    #
    #                             input("\nSexo alterado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
    #                             break
    #                     except Exception as e:
    #                         os.system('cls')
    #                         print(f"Erro: {e}")
    #
    #             elif opcao == 9:
    #                 os.system('cls')
    #                 print("Retornando ao menu principal...")
    #                 time.sleep(3)
    #
    #             else:
    #                 os.system('cls')
    #                 print("Opção inválida!")
    #                 time.sleep(3)
    #
    #         elif op_decisao == 2:
    #             os.system('cls')
    #             print("Retornando ao menu principal...")
    #             time.sleep(3)
    #
    #         else:
    #             os.system('cls')
    #             print("Opção inválida!")
    #             time.sleep(3)














