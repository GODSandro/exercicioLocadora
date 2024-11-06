from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

codigoRemover = int(input('digite o codigo para remover: '))

consultaRemover = 'delete from filmes where codigo = %$'
valores = [codigoRemover]

linhasAfetadas = excluirBancoDados(conexao, consultaRemover, valores)

if linhasAfetadas > 0:
    print('Filme removido com sucesso!')
else:
    print("Não existe filme para para o codigo informado!")

encerrarConexao(conexao)