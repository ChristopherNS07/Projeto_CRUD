import os
import time
from tabulate import tabulate
from IPython.core.display_functions import display
class MedicoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_medico(self, medico):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO TB_MEDICO (CRM, CPF_MEDICO, RG_MEDICO, NOME_MEDICO, EMAIL_MEDICO, "\
                   "ESPECIALIDADE_MEDICO, DTADM_MEDICO, DTDEM_MEDICO, "\
                    "STATUS_MEDICO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            valores = (medico.crm, medico.cpf_medico, medico.rg_medico, medico.nome_medico, medico.email_medico, medico.especialidade_medico,
                       medico.dtadm_medico, medico.dtdem_medico, medico.status_medico)

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()

            os.system("cls")
            print("Medico cadastrado com Sucesso!")
            time.sleep(3)

        except Exception as e:
            print("Erro: ", e)