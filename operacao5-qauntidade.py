from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

consultaQuantidade = 'selec count(*) from filmes'
listagem = listarBancoDados(conexao,consultaQuantidade)
quantidade = listagem[0][0]
print('Atualmente temos' , quantidade, 'filmes(s)')

encerrarConexao(conexao)