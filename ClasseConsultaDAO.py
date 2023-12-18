import os
import time
import mysql.connector
from tabulate import  tabulate
from IPython.core.display_functions import display
class ConsultaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_consulta(self, consulta):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO TB_CONSULTA (COD_CONSULTA, DT_CONSULTA, HR_CONSULTA, ID_MEDICO, ID_PACIENTE) VALUES " \
                  "(%s, %s, %s, %s, %s)"

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

