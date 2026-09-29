from faker import Faker
import random

from aluno import Aluno


class GeradorAlunos:

    def __init__(self):

        self.fake = Faker("pt_BR")

        self.cursos = [
            "Sistemas de Informacao",
            "Engenharia de Computacao",
            "Ciencia da Computacao",
            "Administracao",
            "Engenharia de Producao",
            "Matematica",
            "Direito"
        ]

    def criar_aluno(self, matricula):

        nome_mae = self.fake.name()
        nome_pai = self.fake.name()

        sobrenome_mae = nome_mae.split()[-1]
        sobrenome_pai = nome_pai.split()[-1]

        nome_aluno = (
            self.fake.first_name()
            + " "
            + sobrenome_pai
            + " "
            + sobrenome_mae
        )

        return Aluno(
            matricula,
            nome_aluno,
            self.fake.cpf(),
            random.choice(self.cursos),
            nome_mae,
            nome_pai,
            random.randint(2015, 2026),
            round(random.uniform(0, 10), 2)
        )

    def gerar(self, quantidade):

        alunos = []

        for i in range(quantidade):

            matricula = 100000000 + i

            aluno = self.criar_aluno(matricula)

            alunos.append(aluno)

        return alunos
