class Estatisticas:

    def mostrar(self, blocos, tamanho_bloco):

        if len(blocos) == 0:

            print("Nenhum bloco foi utilizado.")

            return

        total_bytes = 0
        blocos_parciais = 0

        print("\nMAPA DE OCUPAÇÃO")
        print("-------------------------")

        for i, bloco in enumerate(blocos):

            ocupado = len(bloco)

            percentual = (
                ocupado / tamanho_bloco
            ) * 100

            total_bytes += ocupado

            if ocupado < tamanho_bloco:

                blocos_parciais += 1

            print(
                f"Bloco {i + 1}: "
                f"{ocupado} bytes "
                f"({percentual:.2f}% cheio)"
            )

        quantidade_blocos = len(blocos)

        ocupacao_media = ( total_bytes/ (quantidade_blocos * tamanho_bloco)) * 100

        print("\nESTATÍSTICAS")
        print("-------------------------")

        print(
            "Total de blocos:", quantidade_blocos  )

        print(
            f"Ocupação média: "
            f"{ocupacao_media:.2f}%"
        )

        print( "Blocos parcialmente utilizados:", blocos_parciais
        )

        print( f"Eficiência: " f"{ocupacao_media:.2f}%" )
