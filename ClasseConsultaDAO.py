import os
import time
import mysql.connector


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