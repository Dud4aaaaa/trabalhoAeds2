from gerador_alunos import GeradorAlunos
from armazenamento import Armazenamento
from estatistica import Estatisticas


def main():
    quantidade = int(input("Digite a quantidade de alunos: "))
    gerador = GeradorAlunos()

    alunos = gerador.gerar(quantidade)

    print("Alunos gerados com sucesso!")

    tamanho_bloco = int(
        input( "o tamanho do bloco (bytes): ") )

    
    print("\nEscolha o modo de armazenamento:")

    print("1 - Tamanho fixo")
    print("2 - Tamanho variável")

    modo = int(input("Digite sua opção: ") )

    armazenamento = Armazenamento( tamanho_bloco )


    if modo == 1:

        blocos = armazenamento.armazenamento_fixo(alunos )
        nome_arquivo = "alunos_fixo.dat"
    elif modo == 2:

        print("Escolha o tipo:")

        print("1 - Contíguo")
        print("2 - Espalhado")

        tipo = int( input("\nDigite sua opção: "))

        if tipo == 1:

            blocos = (armazenamento.armazenamento_variavel_contiguo( alunos ) )

            nome_arquivo = ( "alunos_variavel_contiguo.dat" )

        elif tipo == 2:

            blocos = (armazenamento.armazenamento_variavel_espalhado(alunos))

            nome_arquivo = ( "alunos_variavel_espalhado.dat" )

        else:

            print("Opção inválida.")

            return

    else:

        print("Opção inválida.")

        return

  
    armazenamento.salvar( blocos,nome_arquivo)

    print("Arquivo salvo:", nome_arquivo)

   
    estatisticas = Estatisticas()

    estatisticas.mostrar( blocos,tamanho_bloco)


if __name__ == "__main__":

    main()
