from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

codigoPesquisa = int(input("Digite o código: "))
consultaListar = 'select * from filmes where codigo = %s'
dados = [codigoPesquisa]

filmes = listarBancoDados(conexao,consultaListar,dados)

if len(filmes) > 0:
    print(filmes[0][1], '»' ,filmes[0][2] )
else:
    print('Não existe filme pra o codigo informado!')

encerrarConexao(conexao)