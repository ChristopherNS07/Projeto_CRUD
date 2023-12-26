import os
import sys
import time
import ClasseConexaoBD as conexao
import ClasseMedico as medico
import ClassePaciente as paciente
import ClasseConsulta as consulta
import ClassePacienteDAO
import ClasseMedicoDAO
import ClasseConsultaDAO
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
        print("1. Cadastrar\n2. Editar Cadastro\n3. Consultar Cadastro\n4. Excluir Cadastro\n5. Desligar Médico"
              "\n6. Religar Médico\n0. Voltar ao Menu Principal")
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
            case 2:
                print("*** Editar registro do médico ***")
                crm_procurado = input("CRM: ")
                os.system("cls")
                medicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                medicoDAO_instancia.editar_medico(crm_procurado)


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

            case 5:
                print("*** Desligar Médico ***")
                crm_procurado = input("Digite o CRM do médico: ")
                os.system("cls")

                medicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                medicoDAO_instancia.desligar_medico(crm_procurado)

            case 6:
                print("*** Religar Médico ***")
                crm_procurado = input("Digite o CRM do médico: ")
                os.system("cls")

                medicoDAO_instancia = ClasseMedicoDAO.MedicoDAO(conexao)
                medicoDAO_instancia.religar_medico(crm_procurado)

    elif op_menu_principal == 3:
        print("***** ÁREA DE CONSULTAS *****")
        op_menu_secundario = int(input("\n1. Marcar Consulta\n2. Editar Consulta\n3. Visualizar Consulta\n4. Desmarcar Consulta\n5. Desvincular Consulta\n0. Voltar ao Menu Pricipal \n\nDigite uma opção: "))
        os.system("cls")  # Comando para limpar a tela



        match op_menu_secundario:
            case 1:
                print("*** Marcar Consulta ***")
                crm_medico = input("\CRM: ")

                sql = "SELECT ID FROM TB_MEDICO WHERE CRM = %s"
                cursor.execute(sql, (crm_medico,))
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
                            cod_consulta = input("Digite o codigo da consulta: ")

                            sql = "SELECT COD_CONSULTA FROM TB_CONSULTA WHERE COD_CONSULTA = %s"
                            cursor.execute(sql, (cod_consulta,))
                            resultado = cursor.fetchall()

                            if len(resultado) != 0:
                                os.system('cls')
                                print("Já existe comsulta cadastrada com este codigo. tente novamente...")
                                time.sleep(3)
                            else:
                                dt_consulta = input("Data da Consulta (YYYY-MM-DD): ")
                                hr_consulta = input("Hora da Cosulta (HH:MM:SS): ")

                                sql = ("SELECT DT_CONSULTA, HR_CONSULTA FROM TB_CONSULTA WHERE (ID_MEDICO = %s OR ID_PACIENTE = %s) "
                                       "AND DT_CONSULTA = %s AND HR_CONSULTA = %s")

                                valores = (id_medico, id_paciente, dt_consulta, hr_consulta)
                                cursor.execute(sql, valores)
                                resultado = cursor.fetchall()

                                if len(resultado) != 0:
                                    os.system('cls')
                                    print("Médico ou paciente não possuem dia/horário disponivel para marcação da cosulta")
                                    input("\nPressione uma tecla para retornar...")

                                else:
                                    nova_consulta = consulta.Consulta(cod_consulta=cod_consulta,
                                                                      dt_consulta=dt_consulta,
                                                                      hr_consulta=hr_consulta,
                                                                      id_medico=id_medico,
                                                                      id_paciente=id_paciente)
                                    consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                                    consultaDAO_instancia.cadastrar_consulta(nova_consulta)

            case 2:
                print("*** Editar Consulta ***")
                cod_consulta = input("Digite o código da consulta: ")
                os.system('cls')
                consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                consultaDAO_instancia.editar_consulta(cod_consulta)

            case 3:
                print("*** Visualizar Consulta ***")
                op_consulta = int(input('\n1 - Consulta única\n2 - Consulta total\n\nDigite uma opção: '))
                os.system('cls')
                if op_consulta == 1:
                    cod_consulta = input("Digite o codigo da consulta a ser alterado: ")
                    consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                    consultaDAO_instancia.visualizar_consulta(cod_consulta)
                elif op_consulta == 2:
                    consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                    consultaDAO_instancia.visualizar_total_consultas()
                else:
                    print("Digito inválido!")
                    time.sleep(3)

            case 4:
                print("*** Desmarcar Consulta ***")
                cod_consulta = input("\nDigite o código da consulta: ")
                os.system('cls')
                consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                consultaDAO_instancia.desmarcar_consulta(cod_consulta)

            case 5:
                print("*** Desvincular Consultas ***")
                op_menu_secundario = int(input("\n1. Por médico\n2. Por paciente\n0. Voltar\n\nEscolha uma opção: "))
                os.system('cls')

                consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
                consultaDAO_instancia.desvincular_medico(op_menu_secundario)

    elif op_menu_principal == 4:
        print("** Agenda **")
        op_menu_secundario = int(input("\n1. Agenda por Paciente\n2. Agenda por Médico\n3. Agenda por Período\n"
                                       "4. Agenda por Horário\n5. Agenda por Paciente + Período\n6. Agenda por "
                                       " Médico + Período\n7. Agenda por horário + periodo\n0. Voltar ao Menu\n\n"
                                       "Escolha uma opção: "))
        os.system('cls')

        consultaDAO_instancia = ClasseConsultaDAO.ConsultaDAO(conexao)
        consultaDAO_instancia.consultar_agenda(op_menu_secundario)

    elif op_menu_principal == 0:
        print("Encerrando sistema...")
        time.sleep(3)
        sys.exit() #Forçar encerramento do programa

    else:
        print("Opção inválida!")
        time.sleep(2)