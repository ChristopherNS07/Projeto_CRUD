import os
import time
import mysql.connector
import pandas as pd
from datetime import datetime
from tkinter import filedialog
from tabulate import  tabulate
from IPython.core.display_functions import display
class ConsultaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_consulta(self, consulta):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = '''INSERT INTO TB_CONSULTA (COD_CONSULTA, DT_CONSULTA, HR_CONSULTA, ID_MEDICO, ID_PACIENTE) VALUES 
                  (%s, %s, %s, %s, %s)'''

            valores = (consulta.cod_consulta, consulta.dt_consulta, consulta.hr_consulta, consulta.id_medico,
                       consulta.id_paciente)

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()

            os.system("cls")
            print("Consulta cadastrada com sucesso!")
            time.sleep(3)

        except Exception as e:
            print("Erro: ", e)
            input("\nPressione uma tecla para continuar...")

    def desmarcar_consulta(self, cod_consulta):
        cursor = self.conexao.conexao.cursor()
        sql = '''SELECT tb_consulta.COD_CONSULTA, tb_consulta.DT_CONSULTA, tb_consulta.HR_CONSULTA,
                 tb_medico.NOME_MEDICO, tb_paciente.NOME_PACIENTE
                 FROM TB_CONSULTA
                 INNER JOIN  TB_MEDICO ON TB_CONSULTA.ID_MEDICO = TB_MEDICO.ID
                 INNER JOIN TB_PACIENTE ON TB_CONSULTA.ID_PACIENTE = TB_PACIENTE.ID
                 WHERE TB_CONSULTA.COD_CONSULTA = %s'''

        try:
            cursor.execute(sql, (cod_consulta,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                os.system('cls')
                print('Consulta não Encontrada!')
                time.sleep(3)

            else:
                resultados = []

                for result in resultado:
                    result = list(result)
                    resultados.append(result)

                colunas = ['COD_CONSULTA', 'DT_CONSULTA', 'HR_CONSULTA', 'ID_MEDICO', 'ID_PACIENTE']
                tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
                display(tabela)


                op_desmarcar = int(input("\nDeseja desmarcar esta cosulta?\n1 - Sim ou 2 - Não\n\n Escolha uma opção: "))
                os.system('cls')

                if op_desmarcar == 1:
                    sql = "DELETE FROM TB_CONSULTA WHERE COD_CONSULTA = %s"
                    cursor.execute(sql, (cod_consulta,))
                    self.conexao.conexao.commit()
                    input("\nConsulta desmarcada com sucesso!\nPressione uma tecla para continuar...")

                elif op_desmarcar == 2:
                    print("Retornando ao meu principal...")
                    time.sleep(2)

                else:
                    print("Opção inválida!")
                    time.sleep(2)

        except Exception as e:
            print("Erro: ", e)
            input("\nPressione uma tecla para retornar...")

    def visualizar_consulta(self, cod_consulta):

        cursor = self.conexao.conexao.cursor()
        sql = '''SELECT tb_consulta.COD_CONSULTA, tb_consulta.DT_CONSULTA, tb_consulta.HR_CONSULTA,
                 tb_medico.NOME_MEDICO, tb_paciente.NOME_PACIENTE
                 FROM TB_CONSULTA
                 INNER JOIN  TB_MEDICO ON TB_CONSULTA.ID_MEDICO = TB_MEDICO.ID
                 INNER JOIN TB_PACIENTE ON TB_CONSULTA.ID_PACIENTE = TB_PACIENTE.ID
                 WHERE TB_CONSULTA.COD_CONSULTA = %s'''

        try:
                cursor.execute(sql, (cod_consulta,))
                resultado = cursor.fetchall()

                if len(resultado) == 0:
                    os.system('cls')
                    print('Consulta não encontrada!\n')
                    time.sleep(3)

                else:
                    resultados = []

                    for result in resultado:
                        result = list(result)
                        resultados.append(result)

                    colunas = ['COD_CONSULTA', 'DT_CONSULTA', 'HR_CONSULTA', 'NOME_MEDICO','NOME_PACIENTE']
                    tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
                    display(tabela)

                    op_csv = int(
                        input("\nDeseja exportar um relatório em CSV?\n1 - Sim ou 2 - Não\n\nEscolha uma opção: "))

                    if op_csv == 1:
                        df = pd.DataFrame(resultados[1:], columns=resultados[0])
                        caminho = filedialog.askdirectory(title="Escolha o diretório")

                        if caminho:
                            nome_arquivo = input("\nDigite um nome para o arquivo: ")
                            df.to_csv((caminho + '/' + nome_arquivo + '.csv'), index=False, encoding='utf-8-sig')

                            print("Tabela Exportada!")

                        else:
                            print("Operação cancelada pelo usuário.")

                    input("\nPressione uma tecla para voltar ao menu principal...\n")

        except Exception as e:
            print('Erro: ', e)

    def visualizar_total_consultas(self):

        cursor = self.conexao.conexao.cursor()
        sql = '''SELECT tb_consulta.COD_CONSULTA, tb_consulta.DT_CONSULTA, tb_consulta.HR_CONSULTA,
                                        tb_medico.NOME_MEDICO, tb_paciente.NOME_PACIENTE
                                        FROM TB_CONSULTA
                                        INNER JOIN  TB_MEDICO ON TB_CONSULTA.ID_MEDICO = TB_MEDICO.ID
                                        INNER JOIN TB_PACIENTE ON TB_CONSULTA.ID_PACIENTE = TB_PACIENTE.ID '''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        resultados = []

        for result in resultado:
            result = list(result)
            resultados.append(result)

        colunas = ['COD_CONSULTA', 'DT_CONSULTA', 'HR_CONSULTA', 'NOME_MEDICO', 'NOME_PACIENTE']
        tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
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

        input("\nPressione uma tecla para voltar ao menu principal...")

    def editar_consulta(self, cod_consulta):
        cursor = self.conexao.conexao.cursor()
        sql = '''SELECT COD_CONSULTA FROM TB_CONSULTA WHERE COD_CONSULTA = %s'''

        try:
            cursor.execute(sql, (cod_consulta,))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                print('Consulta não encontrada!')
                time.sleep(3)

            else:
                novo_cod_consulta = input("Código da consulta: ")
                cursor.execute(sql, (novo_cod_consulta,))
                resultado = cursor.fetchall()

                if len(resultado) != 0 and (novo_cod_consulta != cod_consulta):
                    os.system('cls')
                    print('Código de consulta já existente!')
                    time.sleep(3)

                else:
                    nova_data = input("Data da consulta(YYYY-MM-DD) : ")

                    nova_hr_consulta = input('Digite a hora da consulta (HH:MM:SS): ')
                    sql = '''SELECT HR_CONSULTA FROM TB_CONSULTA WHERE HR_CONSULTA = %s'''
                    cursor.execute(sql, (nova_hr_consulta,))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0 and ((nova_hr_consulta,) in resultado) or len(resultado) == 0:

                        novo_medico = input("CRM: ")
                        sql = "SELECT ID FROM TB_MEDICO WHERE CRM = %s"
                        cursor.execute(sql, (novo_medico,))
                        resultado = cursor.fetchall()

                        if len(resultado) == 0:
                            os.system('cls')
                            print('Médico não encontrado!')
                            time.sleep(3)
                        else:
                            id_medico = resultado[0][0]

                            sql = "SELECT STATUS_MEDICO FROM TB_MEDICO WHERE ID = %s"
                            cursor.execute(sql, (id_medico,))
                            resultado = cursor.fetchall()
                            status_medico = resultado[0][0]
                            # Validação do status do médico, se for inativo não permitir cadastro
                            if status_medico == 'Inativo':
                                print("Não é possivel marcar consultas para este médico, pois ele possui o status Inativo!")
                                time.sleep(3)

                            else:
                                cpf_paciente = input("CPF do paciente: ")

                                sql = "SELECT ID FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"
                                cursor.execute(sql, (cpf_paciente,))
                                resultado = cursor.fetchall()

                                if len(resultado) == 0:
                                    os.system('cls')
                                    print("Paciente não encontrado!")
                                    time.sleep(3)
                                else:
                                    id_paciente = resultado[0][0]

                                    sql = '''UPDATE TB_CONSULTA SET COD_CONSULTA = %s, DT_CONSULTA = %s, 
                                          HR_CONSULTA = %s, ID_MEDICO = %s, ID_PACIENTE = %s WHERE COD_CONSULTA = %s'''
                                    valores = (novo_cod_consulta, nova_data, nova_hr_consulta, id_medico, id_paciente,
                                               cod_consulta)
                                    try:
                                        cursor.execute(sql, valores)
                                        self.conexao.conexao.commit()
                                        os.system("cls")
                                        print(cursor.rowcount, "consulta alterada.")
                                        time.sleep(2)

                                    except Exception as e:
                                        print("Erro: ", e)
                    else:
                        print("Horário indisponivel.\nRetornando ao menu principal...")
                        time.sleep(2)

        except Exception as e:
            print("Erro: ", e)

    def desvincular_medico(self, op_menu):
        cursor = self.conexao.conexao.cursor()

        if op_menu == 1:
            print("OBS: As consultas desvinculadas de um médico deverão ser atribuidas a outro médico dentro do sistema.")
            crm_medico = input("\nDigite o CRM do médico:")

            try:
                sql = '''SELECT ID FROM TB_MEDICO WHERE CRM = %s'''
                cursor.execute(sql, (crm_medico,))
                resultado = cursor.fetchall()

                if len(resultado) == 0:
                    os.system('cls')
                    print("Médico não encontrado!")
                    time.sleep(3)

                else:
                    id_medico = resultado[0][0]
                    dt_inicial = input("Data inicial: ")
                    dt_final = input("Data final: ")

                    dt_inicial = datetime.strptime(dt_inicial, "%Y-%m-%d")
                    dt_final = datetime.strptime(dt_final, "%Y-%m-%d")

                    if dt_inicial > dt_final:
                        os.system('cls')
                        print("Data final não poderá ser menor que a data inicial.")
                        time.sleep(3)

                    else:

                        # Verificar se existem consultas para o médico neste período e se existir, pegar os dados
                        #  de todas as consultas

                        sql = ''' SELECT TB_CONSULTA.COD_CONSULTA, TB_CONSULTA.DT_CONSULTA, TB_CONSULTA.HR_CONSULTA,
                                  TB_MEDICO.NOME_MEDICO, TB_PACIENTE.NOME_PACIENTE FROM TB_CONSULTA
                                  INNER JOIN TB_MEDICO ON TB_CONSULTA.ID_MEDICO = TB_MEDICO.ID
                                  INNER JOIN TB_PACIENTE ON TB_CONSULTA.ID_PACIENTE = TB_PACIENTE.ID
                                  WHERE TB_CONSULTA.ID_MEDICO = %s AND TB_CONSULTA.DT_CONSULTA >= %s
                                  AND TB_CONSULTA.DT_CONSULTA <= %s
                                  ORDER BY DT_CONSULTA, HR_CONSULTA ASC'''

                        valores = (id_medico, dt_inicial, dt_final)
                        cursor.execute(sql, valores)
                        resultado_consultas = cursor.fetchall()

                        if len(resultado_consultas) == 0:
                            os.system('cls')
                            print("Não há consultas para o médico e periodo selecionados.")
                            time.sleep(3)

                        else:
                            resultados = []

                            for result in resultado_consultas:
                                result = list(result)
                                resultados.append(result)

                            colunas = ['COD. CONSULTA', 'DATA CONSULTA', 'HORA CONSULTA', 'MÉDICO', 'PACIENTE']
                            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
                            display(tabela)

                            op_desvinculo = int(input("\nDeseja vincular estas consultas a outro médico?\n1- Sim ou "
                                                      "2 - Não: "))
                            os.system('cls')

                            if op_desvinculo == 1:
                                crm_novo_medico = input("Digite o CRM do novo médico: ")
                                sql = ''' SELECT ID, NOME_MEDICO, STATUS_MEDICO FROM TB_MEDICO WHERE CRM = %s'''
                                cursor.execute(sql, (crm_novo_medico,))
                                resultado_medicos = cursor.fetchall()

                                if len(resultado_medicos) == 0:
                                    os.system('cls')
                                    print("Médico não encontrado!")
                                    time.sleep(3)

                                else:
                                    id_novo_medico = resultado_medicos[0][0]
                                    nome_medico = resultado_medicos[0][1]
                                    status_medico = resultado_medicos[0][2]

                                    if status_medico == "Inativo":
                                        os.system(3)
                                        print(f"O médico {nome_medico} não poderá ser atribuído, pois possui o"
                                              f"cadastro {status_medico}")

                                        time.sleep(3)

                                    else:
                                        index = 0

                                    # Iterando os elementos na lista (percorrendo) -> vetor, array (looping)
                                    for result in resultado_consultas:
                                        cod_consulta = resultado_consultas[index][0]
                                        dt_consulta = resultado_consultas[index][1]
                                        hr_consulta = resultado_consultas[index][2]

                                        sql = '''SELECT * FROM TB_CONSULTA 
                                                 WHERE ID_MEDICO = %s
                                                 AND DT_CONSULTA = %s
                                                 AND HR_CONSULTA = %s'''

                                        valores = (cod_consulta, dt_consulta, hr_consulta)
                                        cursor.execute(sql, valores)
                                        resultado = cursor.fetchall()

                                        if len(resultado) != 0:
                                            os.system('cls')
                                            print(f"O médico {nome_medico} não possuoi horário disponível para"
                                                  f"a atribuição da consulta {cod_consulta}")

                                        else:
                                            sql = '''UPDATE TB_CONSULTA SET ID_MEDICO = %s WHERE COD_CONSULTA = %s'''
                                            valores = (id_novo_medico, cod_consulta)
                                            cursor.execute(sql, valores)
                                            self.conexao.conexao.commit()

                                            print(f"Consulta {cod_consulta} atribuida para o "
                                                  f"médico {nome_medico} com sucesso!")

                                            index += 1

                                    input("\nPressione enter para continuar...")

                            elif op_desvinculo == 2:
                                os.system('cls')
                                print("Retornando ao menu...")
                                time.sleep(3)

                            else:
                                os.system('cls')
                                print("Opção inválida!")
                                time.sleep(3)

            except Exception as e:
                print("Erro: ", e)
                input("\nPressione enter para retornar...")

        if op_menu == 2:
            cpf_paciente = input("Digite o cpf do paciente: ")
            sql = "SELECT ID, NOME_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"

            try:
                cursor.execute(sql, (cpf_paciente,))
                resultado = cursor.fetchall()

                if len(resultado) == 0:
                    os.system('cls')
                    print("Paciente não encontrado!")
                    time.sleep(3)
                else:
                    id_paciente = resultado[0][0]
                    nome_paciente = resultado[0][1]
                    dt_inicial = input("Data inicial: ")
                    dt_final = input("Data final: ")

                    dt_inicial = datetime.strptime(dt_inicial, "%Y-%m-%d")
                    dt_final = datetime.strptime(dt_final, "%Y-%m-%d")

                    if dt_inicial > dt_final:
                        os.system('cls')
                        print("Data final não poderá ser menor que a data inicial.")
                        time.sleep(3)

                    else:
                        sql = '''SELECT TB_CONSULTA.COD_CONSULTA, TB_CONSULTA.DT_CONSULTA, TB_CONSULTA.HR_CONSULTA,
                                 TB_MEDICO.NOME_MEDICO, TB_PACIENTE.NOME_PACIENTE FROM TB_CONSULTA
                                 INNER JOIN TB_MEDICO ON TB_CONSULTA.ID_MEDICO = TB_MEDICO.ID
                                 INNER JOIN TB_PACIENTE ON TB_CONSULTA.ID_PACIENTE = TB_PACIENTE.ID
                                 WHERE ID_PACIENTE = %s AND TB_CONSULTA.DT_CONSULTA >= %s
                                 AND TB_CONSULTA.DT_CONSULTA <= %s
                                 ORDER BY DT_CONSULTA, HR_CONSULTA ASC'''

                        valores = (id_paciente, dt_inicial, dt_final,)
                        cursor.execute(sql, valores)
                        resultado_paciente = cursor.fetchall()

                        if len(resultado_paciente) == 0:
                            os.system('cls')
                            print('Não existe consulta atrelada ao paciente.')
                            time.sleep(3)
                        else:

                            resultados = []

                            for result in resultado_paciente:
                                result = list(result)
                                resultados.append(result)


                            colunas = ['COD CONSULTA', 'DATA CONSULTA', 'HR_CONSULTA', 'NOME MÉDICO', 'NOME PACIENTE']
                            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
                            display(tabela)

                            op_decisao = int(input(f"\nDeseja desmarcar a consulta vinculada ao paciente {nome_paciente} ?\n"
                                                   "OBS.: as consultas serão excluídas do sistema."
                                                   "\n1 - Sim\n2 - Não\n\nDigite uma opção:  "))
                            if op_decisao == 1:
                                sql = "DELETE FROM TB_CONSULTA WHERE ID_PACIENTE = %s"
                                cursor.execute(sql, (id_paciente,))
                                self.conexao.conexao.commit()
                                input(f"\nConsulta do paciente {nome_paciente} desmarcada com sucesso!"
                                      f"\nPressione uma tecla para continuar...")

                            elif op_decisao == 2:
                                print("Retornando ao menu principal...")
                                time.sleep(3)

                            else:
                                print("\Opção inválida!")
                                time.sleep(3)

            except Exception as e:
                print("Erro: ", e)
                time.sleep(3)

        elif op_menu == 0:
            print("Retornando ao menu principal...")
            time.sleep(3)

        else:
            os.system('cls')
            print("Retornando ao menu principal...")
            time.sleep(3)








