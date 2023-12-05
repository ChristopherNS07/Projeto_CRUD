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