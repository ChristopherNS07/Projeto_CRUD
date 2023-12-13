import os
import sys
import time
import ClasseConexaoBD as conexao
import ClasseMedico as medico
import ClassePaciente as paciente
import ClassePacienteDAO
import ClasseMedicoDAO
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
            case 2:
                print("*** Editar cadastro do paciente ***")
                cpf_procurado = input("\nCPF: ")
                pacienteDAO_instancia = ClassePacienteDAO.PacienteDAO(conexao)
                pacienteDAO_instancia.editar_paciente(cpf_procurado)

            case 3:
                print("*** Consulta ao cadastro de pacientes ***")
                op_consulta = int(input("\n1. Consulta Única por CPF\n2. Consulta total\n0. Voltar ao "
                                  "Menu\n\nEscolha uma opção: "))
                os.system("cls")

                if op_consulta == 1:
                    cpf_procurado = input("Digite o CPF do Paciente: ")
                    pacienteDAO_instancia = ClassePacienteDAO.PacienteDAO(conexao)
                    pacienteDAO_instancia.consultar_paciente(cpf_procurado)

                elif op_consulta == 2:
                    pacienteDAO_instancia = ClassePacienteDAO.PacienteDAO(conexao)
                    pacienteDAO_instancia.consultar_todos_pacientes()

                elif op_consulta == 0:
                    pass # passa para a próxima rotina

                else:
                    print("Opção inválida\n\nRetornando ao menu principal...")
                    time.sleep(3)

            case 4:
                print("*** Exclusão de paciente ***")
                cpf_procurado_paciente = input("\nCPF: ")
                pacienteDAO_instancia = ClassePacienteDAO.PacienteDAO(conexao)
                pacienteDAO_instancia.excluir_pacientes(cpf_procurado_paciente)

            case 0:
                pass # Voltar ao menu principal

            case _:
                print("Opção inválida !")
                time.sleep(2)

    elif op_menu_principal == 2:
        print("***** ÁREA DE MÉDICOS *****")
        print("1. Cadastrar\n2. Editar Cadastro\n3. Consultar Cadastro\n4. Excluir Cadastro\n0. Voltar ao Menu "
              "Principal")
        op_menu_secundario = int(input("\nDigite uma opção: "))
        os.system("cls")

    match op_menu_secundario:
        case 1:
            print("*** Cadastro de Médicos ***")
            crm_medico = input("\nCRM: ")

            sql = 'SELECT CRM FROM TB_MEDICO WHERE CRM = %s'
            cursor.execute(sql, (crm_medico,))
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                os.system("cls")
                print("CRM já cadastrado!")
                time.sleep(3)

            else:

                cpf_medico = input("CPF: ")

                sql = 'SELECT CPF_MEDICO FROM TB_MEDICO WHERE CPF_MEDICO = %s'
                cursor.execute(sql, (cpf_medico,))
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    os.system("cls")
                    print("CPF já cadastrado!")
                    time.sleep(3)

                else:
                    rg_medico = input("RG: ")

                    sql = 'SELECT RG_MEDICO FROM TB_MEDICO WHERE RG_MEDICO = %s'
                    cursor.execute(sql, (rg_medico,))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0:
                        os.system("cls")
                        print("RG já cadastrado!")
                        time.sleep(3)

                    else:
                        nome_medico = input("Nome: ")
                        email_medico = input("Email: ")
                        especialidade_medico = input("Especialidade: ")
                        dt_admissao = input("Dt Admissão (YYYY-MM-DD): ")
                        dt_demissao = input("Dt demissão (YYYY-MM-DD): ")

                        if not dt_demissao:
                            status_medico = "Ativo"

                        else:
                            status_medico = "Inativo"

                        novo_medico = medico.Medico(crm=crm_medico, cpf=cpf_medico, rg=rg_medico, nome=nome_medico,
                                                    email=email_medico, especialidade=especialidade_medico,
                                                    dt_admissao=dt_admissao, dtdemissao=dt_demissao,
                                                    status=status_medico)
                        medicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                        medicoDAO_instancia.cadastrar_medico(novo_medico)

        case 3:
            print("*** Consulta ao cadastro do médico ***")
            op_consulta = int(input("\n1. Consulta Única por CRM\n2. Consulta total\n0. Voltar ao "
                                    "Menu\n\nEscolha uma opção: "))
            os.system("cls")

            if op_consulta == 1:
                crm_procurado = input("Digite o CRM do Médico: ")
                MedicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                MedicoDAO_instancia.consultar_medico(crm_procurado)

            elif op_consulta == 2:
                MedicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                MedicoDAO_instancia.consultar_todos_medicos()

            elif op_consulta == 0:
                pass  # passa para a próxima rotina

            else:
                print("Opção inválida\n\nRetornando ao menu principal...")
                time.sleep(3)

        case 4:
            print("*** Excluir Médico ***")
            crm_procurado = input("CRM: ")
            MedicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
            MedicoDAO_instancia.excluir_medico(crm_procurado)