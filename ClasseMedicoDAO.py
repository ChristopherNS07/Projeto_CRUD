import os
import time
from tabulate import tabulate
from IPython.core.display_functions import display
import pandas as pd
from tkinter import filedialog
class MedicoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_medico(self, medico):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO TB_MEDICO (CRM, CPF_MEDICO, RG_MEDICO, NOME_MEDICO, EMAIL_MEDICO, "\
                   "ESPECIALIDADE_MEDICO, DTADM_MEDICO, DTDEM_MEDICO, "\
                    "STATUS_MEDICO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            valores = (medico.crm, medico.cpf_medico, medico.rg_medico, medico.nome_medico, medico.email_medico,
                       medico.especialidade_medico, medico.dtadm_medico, medico.dtdem_medico, medico.status_medico)

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()

            os.system("cls")
            print("Medico cadastrado com Sucesso!")
            time.sleep(3)

        except Exception as e:
            print("Erro: ", e)

    def consultar_medico(self, crm_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CRM, NOME_MEDICO, RG_MEDICO, CPF_MEDICO, EMAIL_MEDICO, ESPECIALIDADE_MEDICO," \
               "DTADM_MEDICO, DTDEM_MEDICO, STATUS_MEDICO FROM TB_MEDICO WHERE CRM = %s"

        try:
            cursor.execute(sql, (crm_procurado,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system("cls")
                print("Médico não encontrado")
                time.sleep(3)

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result)

                colunas = ['CRM', 'NOME', 'RG', 'CPF', 'EMAIL', 'ESPECIALIDADES', 'DT ADMISSÃO', 'DT DEMISSÃO', 'STATUS']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
                display(tabela)
                input("\nPressione uma tecla para continuar...")

        except Exception as e:
            print("Erro: ", e)

    def consultar_todos_medicos(self):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CRM, NOME_MEDICO, RG_MEDICO, CPF_MEDICO, EMAIL_MEDICO, ESPECIALIDADE_MEDICO," \
               "DTADM_MEDICO, DTDEM_MEDICO, STATUS_MEDICO FROM TB_MEDICO"

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

                colunas = ['CRM', 'NOME', 'RG', 'CPF', 'EMAIL', 'ESPECIALIDADES', 'DT ADMISSÃO', 'DT DEMISSÃO', 'STATUS']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
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

    def excluir_medico(self, crm_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = ("SELECT CRM, NOME_MEDICO, RG_MEDICO, CPF_MEDICO, EMAIL_MEDICO, ESPECIALIDADE_MEDICO," \
               " DTADM_MEDICO, DTDEM_MEDICO, STATUS_MEDICO FROM tb_medico WHERE CRM = %s")

        try:
            cursor.execute(sql, (crm_procurado,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system('cls')
                print("Médico não encontrado\n Retornando ao menu principal...")
                time.sleep(3)

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result)

                colunas = ['CPF', 'RG', 'NOME', 'ENDERECO', 'CEP', 'CELULAR', 'DT_NASCIMENTO', 'SEXO']
                tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
                display(tabela)
                exclusao = input("Deseja exluir esse Cadastro ?\n\n S - sim ou N - não: ")

                if exclusao.upper() == "S":
                    cursor = self.conexao.conexao.cursor()
                    sql = "DELETE FROM tb_medico WHERE CRM = %s"

                    cursor.execute(sql, (crm_procurado,))
                    self.conexao.conexao.commit()

                    os.system('cls')
                    print("Cadastro excluido com sucesso!")
                    time.sleep(2)
                    input("Pressione uma tecla para continuar...")

                elif exclusao.upper() == "N":
                    print("Retornando ao menu principal...")
                    time.sleep(3)

                else:
                    print("Digito inválido!\n Retornando ao menu principal...")
                    time.sleep(3)

        except Exception as e:
            print("Erro: ", e)





