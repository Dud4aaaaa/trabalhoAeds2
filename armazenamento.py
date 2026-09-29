class Armazenamento:

    def __init__(self, tamanho_bloco):

        self.tamanho_bloco = tamanho_bloco

    def armazenamento_fixo(self, alunos):

        blocos = []
        bloco_atual = bytearray()

        for aluno in alunos:

            registro = self.registro_fixo(aluno)

            if len(registro) > self.tamanho_bloco:

                print(
                    "Erro: registro maior que o tamanho do bloco."
                )

                return []

            if (
                len(bloco_atual) + len(registro)
                > self.tamanho_bloco
            ):

                blocos.append(bloco_atual)

                bloco_atual = bytearray()

            bloco_atual.extend(registro)

        if len(bloco_atual) > 0:

            blocos.append(bloco_atual)

        return blocos

    def registro_fixo(self, aluno):

        matricula = str(aluno.matricula).ljust(9)
        nome = aluno.nome.ljust(50)
        cpf = aluno.cpf.ljust(11)
        curso = aluno.curso.ljust(30)
        mae = aluno.filiacao_mae.ljust(30)
        pai = aluno.filiacao_pai.ljust(30)
        ano = str(aluno.ano_ingresso).ljust(4)
        ca = f"{aluno.ca:.2f}".ljust(5)

        dados = (
            matricula + "|" +
            nome + "|" +
            cpf + "|" +
            curso + "|" +
            mae + "|" +
            pai + "|" +
            ano + "|" +
            ca
        )

        return dados.encode("utf-8")

    def armazenamento_variavel_contiguo(self, alunos):

        blocos = []
        bloco_atual = bytearray()

        for aluno in alunos:

            registro = aluno.para_bytes()

            if len(registro) > self.tamanho_bloco:

                print(
                    "Erro: registro maior que o tamanho do bloco."
                )

                return []

            if (
                len(bloco_atual) + len(registro)
                > self.tamanho_bloco
            ):

                blocos.append(bloco_atual)

                bloco_atual = bytearray()

            bloco_atual.extend(registro)

        if len(bloco_atual) > 0:

            blocos.append(bloco_atual)

        return blocos

    def armazenamento_variavel_espalhado(self, alunos):

        blocos = []
        bloco_atual = bytearray()

        for aluno in alunos:

            registro = aluno.para_bytes()

            posicao = 0

            while posicao < len(registro):

                espaco = (
                    self.tamanho_bloco
                    - len(bloco_atual)
                )

                if espaco == 0:

                    blocos.append(bloco_atual)

                    bloco_atual = bytearray()

                    espaco = self.tamanho_bloco

                quantidade = min(
                    espaco,
                    len(registro) - posicao
                )

                bloco_atual.extend(
                    registro[
                        posicao:posicao + quantidade
                    ]
                )

                posicao += quantidade

        if len(bloco_atual) > 0:

            blocos.append(bloco_atual)

        return blocos

    def salvar(self, blocos, nome_arquivo):

        with open(nome_arquivo, "wb") as arquivo:

            for bloco in blocos:

                arquivo.write(bloco)
