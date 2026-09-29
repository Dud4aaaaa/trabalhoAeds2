class Aluno:

    def __init__(
        self,
        matricula,
        nome,
        cpf,
        curso,
        filiacao_mae,
        filiacao_pai,
        ano_ingresso,
        ca
    ):

        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.filiacao_mae = filiacao_mae
        self.filiacao_pai = filiacao_pai
        self.ano_ingresso = ano_ingresso
        self.ca = ca

    def para_bytes(self):

        dados = (
            str(self.matricula) + "|" +
            self.nome + "|" +
            self.cpf + "|" +
            self.curso + "|" +
            self.filiacao_mae + "|" +
            self.filiacao_pai + "|" +
            str(self.ano_ingresso) + "|" +
            str(self.ca)
        )

        return dados.encode("utf-8")

    def tamanho(self):

        return len(self.para_bytes())

    def __str__(self):

        return (
            f"{self.matricula} | "
            f"{self.nome} | "
            f"{self.cpf} | "
            f"{self.curso} | "
            f"{self.ca}"
        )
