import os
import time


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