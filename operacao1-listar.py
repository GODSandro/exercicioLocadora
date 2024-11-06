from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

filmes = listarBancoDados(conexao, 'select * from filmes')

if len(filmes) > 0:
    print('Lista de filmes')
    for item in filmes:
        print(item[0], '»' ,item[1], ' - ' ,item[3] )
else:
    print("Não existe filmes à exibir")

encerrarConexao(conexao)