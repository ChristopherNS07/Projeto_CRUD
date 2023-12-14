import os
import time
from tabulate import tabulate
from IPython.core.display_functions import display
import pandas as pd
from tkinter import filedialog
from datetime import datetime
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

    def editar_medico(self, crm_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CRM FROM TB_MEDICO WHERE CRM = %s"
        cursor.execute(sql, (crm_procurado,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            os.system("cls")
            print("Médico não encontrado")
            time.sleep(2)

        else:
            novo_crm = input("Novo CRM: ")
            cursor.execute(sql, (novo_crm,))
            resultado = cursor.fetchall()

            if len(resultado) != 0 and novo_crm != crm_procurado:
                os.system("cls")
                print("CRM já cadastrado para outro médico")
                time.sleep(2)

            else:
                cpf_medico = input("CPF: ")

                sql = "SELECT CPF_MEDICO FROM TB_MEDICO WHERE CPF_MEDICO = %s"
                sql2 = "SELECT CPF_MEDICO FROM TB_MEDICO WHERE CRM = %s"

                cursor.execute(sql, (cpf_medico,))
                resultado = cursor.fetchall()

                cursor.execute(sql2, (crm_procurado,))
                resultado2 = cursor.fetchall()

                if (len(resultado) != 0 and ((cpf_medico,) in resultado2)) or len(resultado) == 0:
                    rg_medico = input("RG: ")

                    sql = "SELECT RG_MEDICO FROM TB_MEDICO WHERE RG_MEDICO = %s"
                    sql2 = "SELECT RG_MEDICO FROM TB_MEDICO WHERE CRM = %s"

                    cursor.execute(sql, (rg_medico,))
                    resultado = cursor.fetchall()

                    cursor.execute(sql2, (crm_procurado,))
                    resultado2 = cursor.fetchall()

                    if (len(resultado) != 0 and ((rg_medico,) in resultado2)) or len(resultado) == 0:
                        nome_medico = input("Nome: ")
                        email_medico = input("Email: ")
                        especialidade_medico = input("Especialidade: ")
                        dt_admissao_medico = input("Data de Admissão: ")

                        sql = ("UPDATE TB_MEDICO SET CRM = %s, CPF_MEDICO = %s, RG_MEDICO = %s, NOME_MEDICO = %s," \
                               "EMAIL_MEDICO = %s, ESPECIALIDADE_MEDICO = %s, DTADM_MEDICO = %s WHERE CRM = %s")

                        valores = (novo_crm, cpf_medico, rg_medico, nome_medico, email_medico, especialidade_medico, dt_admissao_medico, crm_procurado)

                        try:
                            cursor.execute(sql, valores)
                            self.conexao.conexao.commit()
                            os.system("cls")
                            print(cursor.rowcount, "registro alterado.")
                            time.sleep(2)

                        except Exception as e:
                            print("Erro: ", e)
                    else:
                        os.system("cls")
                        print("RG já cadastrado em outro médico.")
                        time.sleep(2)
                else:
                    os.system("cls")
                    print("CPF já cadastrado em outro médico")
                    time.sleep(2)

    def desligar_medico(self, crm_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT NOME_MEDICO FROM TB_MEDICO WHERE CRM = %s"

        try:
            cursor.execute(sql, (crm_procurado,))
            nome_medico = cursor.fetchall()

            if len(nome_medico) == 0:
                os.system("cls")
                print("Médico não encontrado!")
                time.sleep(2)

            else:
                op_desligamento = int(input(f"Deseja inativar o médico{nome_medico[0][0]}?\n1 - Sim ou 2 - Não\n\n"))
                data_desligamento = input("Data do Desligamento (YYYY-MM-DD): ")
                data_desligamento = datetime.strptime(data_desligamento, '%Y-%m-%d')

                if op_desligamento == 1:
                    sql = "SELECT ID FROM TB_MEDICO WHERE CRM = %s"
                    cursor.execute(sql, (crm_procurado,))
                    id_medico = cursor.fetchall()

                    sql = "SELECT DT_CONSULTA FROM TB_CONSULTA WHERE ID_MEDICO = %s ORDER BY DT_CONSULTA DESC"
                    cursor.execute(sql, (id_medico[0][0],))
                    resultado = cursor.fetchall()

                    if not resultado:
                        resultado = datetime.strptime(str('1111-11-11'), '%Y-%m-%d')

                    else:
                        resultado = f"{str(resultado[0][0].year)}-{str(resultado[0][0].month)}-{str(resultado[0][0].day)}"
                        resultado = datetime.strptime(resultado, "%Y-%m-%d")

                    if resultado >= data_desligamento:
                        os.system("cls")
                        print("Médico não poderá ser desligado, pois possui consultas vinculadas ao seu cadastro"
                              "com data maior que ou igual à data inserida para o desligamento.")

                        input("\nPressione uma tecla para continuar...")

                    else:
                        os.system("cls")
                        status_medico = "Inativo"
                        sql = "UPDATE TB_MEDICO SET DTDEM_MEDICO =  %s, STATUS_MEDICO = %s WHERE ID = %s"
                        valores = (data_desligamento, status_medico, id_medico[0][0])
                        cursor.execute(sql, valores)
                        self.conexao.conexao.commit()

                        print(f"O médico {nome_medico[0][0]} foi desligado!")
                        input("\nPressione uma tecla para continuar...")

        except Exception as e:
            print("Erro: ", e)

    def religar_medico(self, crm_procurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT NOME_MEDICO FROM TB_MEDICO WHERE CRM = %s"

        try:
            cursor.execute(sql, (crm_procurado,))
            nome_medico = cursor.fetchall()

            if len(nome_medico) == 0:
                os.system("cls")
                print("Médico não encontrado!")
                time.sleep(2)
            else:
                sql = "SELECT STATUS_MEDICO FROM TB_MEDICO WHERE CRM = %s"
                cursor.execute(sql, (crm_procurado,))
                resultado = cursor.fetchall()
                status_medico = resultado[0][0]

                if status_medico == "Ativo":
                    os.system('cls')
                    print('Médico já ativo no sistema.')
                    time.sleep(3)

                else:
                    status_medico = "Ativo"
                    dt_dem_medico = '0000-00-00'

                    sql = "UPDATE TB_MEDICO SET DTDEM_MEDICO = %s, STATUS_MEDICO = %s WHERE CRM = %s"
                    valores = (dt_dem_medico, status_medico, crm_procurado)
                    cursor.execute(sql, valores)
                    self.conexao.conexao.commit()
                    os.system('cls')
                    input("Medico reativado no Sistema!\n\nPressione uma tecla para continuar...")

        except Exception as e:
            print("Erro: ", e)












