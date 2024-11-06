from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

codigoRemover = int(input('Digite o codigo para remover: '))

consultaRemover = 'delete from filmes where codigo = %s'
valores = [codigoRemover]

linhasAfetadas = excluirBancoDados(conexao, consultaRemover, valores)

if linhasAfetadas > 0:
    print('Filme removido com sucesso!')
else:
    print("Não existe filme(s) para para o codigo informado!")

encerrarConexao(conexao)