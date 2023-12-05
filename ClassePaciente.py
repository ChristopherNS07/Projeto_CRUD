class Paciente:
    # Método construtor
    def __init__(self, cpf_paciente, rg_paciente, nome_paciente, endereco_paciente, cep_paciente,
                 celular_paciente, dt_nascimento_paciente, sexo_paciente):
        self.cpf_paciente = cpf_paciente
        self.rg_paciente = rg_paciente
        self.nome_paciente = nome_paciente
        self.endereco_paciente = endereco_paciente
        self.cep_paciente = cep_paciente
        self.celular_paciente = celular_paciente
        self.dt_nascimento_paciente = dt_nascimento_paciente
        self.sexo_paciente = sexo_paciente