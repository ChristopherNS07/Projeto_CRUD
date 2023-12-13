class Medico:
    # Método construtor
    def __init__(self, crm, cpf, rg, nome, email, especialidade, dt_admissao,
                 dt_demissao, status):
        self.crm = crm
        self.cpf_medico = cpf
        self.rg_medico = rg
        self.nome_medico = nome
        self.email_medico = email
        self.especialidade_medico = especialidade
        self.dtadm_medico = dt_admissao
        self.dtdem_medico = dt_demissao
        self.status_medico = status