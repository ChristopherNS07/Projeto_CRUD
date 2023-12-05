import os
import sys
import time
import ClasseConexaoBD as conexao
import ClassePaciente as paciente
import ClassePacienteDAO

if __name__ == "__main__":
    conexao = conexao.ConexaoBanco(host="localhost", user="root", password="", database="clinimed")

conexao.conectar()

cursor = conexao.conexao.cursor()

while True:
    print("***** CLINIMED *****")
    print("\n1. Área de Pacientes\n2. Área de Médicos\n3. Área de Consultas\n4. Agenda\n0. Sair")
    op_menu_principal = int(input("\nDigite uma opção: "))
    os.system("cls")  # Comando para limpar a tela

    # Implementação da Área de Pacientes
    if op_menu_principal == 1:
        print("***** ÁREA DE PACIENTES *****")
        print("1. Cadastrar\n2. Editar Cadastro\n3. Consultar Cadastro\n4. Excluir Cadastro\n0. Voltar ao Menu "
              "Principal")
        op_menu_secundario = int(input("\nDigite uma opção: "))
        os.system("cls")

        match op_menu_secundario:
            case 1:
                print("*** Cadastro de Pacientes ***")
                cpf_paciente = input("\nCPF: ")

                sql = "SELECT CPF_PACIENTE FROM TB_PACIENTE WHERE CPF_PACIENTE = %s"
                cursor.execute(sql, (cpf_paciente,))
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    os.system("cls")
                    print("CPF já está cadastrado em outro Paciente!")
                    time.sleep(2)

                else:
                    rg_paciente = input("RG: ")

                    sql = "SELECT RG_PACIENTE FROM TB_PACIENTE WHERE RG_PACIENTE = %s"
                    cursor.execute(sql, (rg_paciente,))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0:
                        os.system("cls")
                        print("RG já está cadastrado em outro Paciente!")
                        time.sleep(2)

                    else:
                        nome_paciente = input("Nome: ")
                        endereco_paciente = input("Endereço: ")
                        cep_paciente = input("CEP: ")
                        celular_paciente = input("Celular: ")
                        dt_nascimento_paciente = input("Data de Nascimento (YYYY-MM-DD): ")
                        sexo_paciente = input("Sexo (M ou F): ")

                        if sexo_paciente.upper() != 'M' and sexo_paciente.upper() != 'F':
                            os.system("cls")
                            print("Sexo Inválido!")

                        else:
                            # instanciando novo paciente (criando novo paciente)
                            novo_paciente = paciente.Paciente(cpf_paciente=cpf_paciente, rg_paciente=rg_paciente,
                                                              nome_paciente=nome_paciente,
                                                              endereco_paciente=endereco_paciente,
                                                              cep_paciente=cep_paciente,
                                                              celular_paciente=celular_paciente,
                                                              dt_nascimento_paciente=dt_nascimento_paciente,
                                                              sexo_paciente=sexo_paciente)

                            pacienteDAO_instancia = ClassePacienteDAO.PacienteDAO(conexao)
                            pacienteDAO_instancia.cadastrar_paciente(novo_paciente)
