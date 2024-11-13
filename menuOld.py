# opcao = 1
#
# from operecoesbd import *
# conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')
#
# while opcao !=6:
#
#     print(" \n1 » Listar \n2 » Adicinoar \n3 » Pesquisar \n4 » Remover \n5 » Quantidade \n6 » Sair \n")
#
#     opcao = int (input("Digite a sua opção: "))
#
#     if opcao == 1:
#
#         filmes = listarBancoDados(conexao, 'select * from filmes')
#
#         if len(filmes) > 0:
#             print('Lista de filmes')
#             for item in filmes:
#                 print(item[0], '»', item[1], ' - ', item[3])
#         else:
#             print("Não existe filmes à exibir")
#
#     elif opcao == 2:
#
#         nomeFilme = input('Digite o nome do filme: ')
#         sinopseFilme = input('Digite a sinopse do filme: ')
#         anoFilme = input('Digite o ano do filme: ')
#
#         consultaInserir = 'insert into filmes (nome,sinopse,ano) values (%s,%s,%s)'
#         valores = [nomeFilme, sinopseFilme, anoFilme]
#
#         insertNoBancoDados(conexao, consultaInserir, valores)
#         print('Filme inserido com sucesso!')
#
#     elif opcao == 3:
#
#         codigoPesquisa = int(input("Digite o código: "))
#         consultaListar = 'select * from filmes where codigo = %s'
#         dados = [codigoPesquisa]
#
#         filmes = listarBancoDados(conexao, consultaListar, dados)
#
#         if len(filmes) > 0:
#             print(filmes[0][1], '»', filmes[0][2])
#         else:
#             print('Não existe filme pra o codigo informado!')
#
#     elif opcao == 4:
#
#         codigoRemover = int(input('digite o codigo para remover: '))
#
#         consultaRemover = 'delete from filmes where codigo = %s'
#         valores = [codigoRemover]
#
#         linhasAfetadas = excluirBancoDados(conexao, consultaRemover, valores)
#
#         if linhasAfetadas > 0:
#             print('Filme removido com sucesso!')
#         else:
#             print("Não existe filme para para o codigo informado!")
#
#     elif opcao == 5:
#
#         conexao = criarConexao('localhost', 'root', '1234', 'locadora_lessandro')
#
#         consultaQuantidade = 'select count(*) from filmes'
#         listagem = listarBancoDados(conexao, consultaQuantidade)
#         quantidade = listagem[0][0]
#         print('Atualmente temos', quantidade, 'filmes(s)')
#
#     elif opcao != 6:
#         print('Sair')
#
# print('Obrigado por usar nosso software')