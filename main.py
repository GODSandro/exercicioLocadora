from menu import *
from operecoesbd import *

opcao = 1

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

while opcao !=6:

    print(" \n1 » Listar \n2 » Adicinoar \n3 » Pesquisar \n4 » Remover \n5 » Quantidade \n6 » Sair \n")

    opcao = int (input("Digite a sua opção: "))

    if opcao == 1:
        listarFilmes(conexao)

    elif opcao == 2:
        adicinarFilmes(conexao)

    elif opcao == 3:
        pesquisarCodigoFilme(conexao)

    elif opcao == 4:
        removerFilme(conexao)

    elif opcao == 5:
        quantidadeFilme()

    elif opcao != 6:
        print('Sair')


print('Obrigado por usar nosso software')

encerrarConexao(conexao)