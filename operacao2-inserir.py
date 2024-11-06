from operecoesbd import *

conexao = criarConexao('localhost', 'root' , '1234' , 'locadora_lessandro')

nomeFilme = input('Digite o nome do filme: ')
sinopseFilme = input('Digite a sinopse do filme: ')
anoFilme = input('Digite o ano do filme: ')


consultaInserir = 'insert into filmes (nome,sinopse,ano) values (%s,%s,%s)'
valores = [nomeFilme, sinopseFilme, anoFilme]

insertNoBancoDados(conexao,consultaInserir,valores)
print('Filme inserido com sucesso!')

encerrarConexao(conexao)