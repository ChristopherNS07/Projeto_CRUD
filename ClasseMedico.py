class Medico:
    # Método construtor
    def __init__(self, crm, cpf, rg, nome, email, especialidade, dt_admissao,
                 dtdemissao, status):
        self.crm = crm
        self.cpf_medico = cpf
        self.rg_medico = rg
        self.nome_medico = nome
        self.email_medico = email
        self.especialidade_medico = especialidade
        self.dtadm_medico = dt_admissao
        self.dtdem_medico = dtdemissao
        self.status_medico = status