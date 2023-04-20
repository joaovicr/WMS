import tkinter as tk
from tkinter import *
from tkinter.font import Font
import time
import psycopg2
import pyodbc
import pandas as pd
import locale
import numpy
from datetime import datetime, timedelta
# Inicia a contagem do tempo de execução
inicio = time.perf_counter()
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # DEFININDO O PADRÃO DOS DADOS PARA APLICAR A FUNCAO LOCALE
def TabelaRetorna(empresa):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    conn2 = psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms",
                            password="Master100")
    Retorna = pd.read_sql("SELECT codEmpresa, codPedido, vlrSugestao, situacaoSugestao, dataHoraListagem, CONVERT(int,SUBSTRING(dataHoraListagem,1,5)) as DataGeracao,"
                          "CONVERT(int,$PIECE(dataHoraListagem,',',2)) as hora "
                          "from ped.SugestaoPed WHERE dataHoraListagem > 0 and codEmpresa in (" + empresa + ") and situacaoSugestao =2 ",
                          conn)

    df_Pedidos = pd.read_sql("SELECT top 100000 codColecao  ,codPedido, codTipoNota, dataPrevFat, codCliente, codRepresentante,"
                            "descricaoCondVenda, vlrPedido as vlrSaldo,qtdPecasFaturadas FROM Ped.Pedido where codEmpresa in (" + empresa + ") order by codPedido desc ",conn)


    RetornaItens = pd.read_sql(
        "Select codPedido, "
        "(SELECT codItemPai  from cgi.Item2 i WHERE i.Empresa = 1 and i.codItem = ps.produto) as codProduto, "
        "SUM(qtdeSugerida) as sugerido , SUM(qtdePecasConf) as conferido  from ped.SugestaoPedItem ps "
        "WHERE codEmpresa in (" + empresa + ") GROUP by codPedido", conn)

    DistribuicaoColaborador = pd.read_sql('select * from "Reposicao".pedidossituacao p ', conn2)

    RetornaItens = RetornaItens[RetornaItens['conferido'] == 0]
    Retorna = pd.merge(RetornaItens, Retorna, on='codPedido')
    Retorna = pd.merge(Retorna, df_Pedidos, on='codPedido', how='left')
    Retorna = pd.merge(Retorna, DistribuicaoColaborador, on='codPedido', how='left')

    Retorna = Retorna.sort_values(by='codCliente')  # escolher como deseja classificar
    Retorna["sugerido"] = Retorna["sugerido"].astype(int)
    Retorna['MARCA'] = Retorna['codProduto'].apply(lambda x: x[:3])
    Retorna['MARCA'] = numpy.where((Retorna['codProduto'].str[:3] == '102') | (Retorna['codProduto'].str[:3] == '202') , 'M.POLLO', 'PACO')
    Retorna['DataGeracao'] = pd.to_datetime(Retorna['DataGeracao'] , origin='1840-12-31', unit='D')
    Retorna['hora'] = (Retorna['hora']/100000)*24
    Retorna = Retorna.sort_values(by='DataGeracao')  # escolher como deseja classificar
    Retorna['DataGeracao']=  Retorna['DataGeracao'].dt.strftime('%d/%m/%Y')
    Retorna['codcolaborador'] = Retorna['codcolaborador'].replace('', numpy.nan).fillna('')


    Retorna = Retorna.reindex()
    Retorna = Retorna.reset_index(drop=True) # adicionando essa linha para resetar o índice
    conn.close()
    conn2.close()
    return Retorna


def Distribuicao(empresa):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    DistribuicaoColaborador = pd.read_sql('select c.nome, sum(p.qtdepedida)as total_peças, '
                                          'count(p."codPedido") as Pedido,'
                                          ' (sum(p.qtdepedida) /count(p."codPedido")) as Media '
                                          ' from "Reposicao".cadusuarios c '
                                          'left join "Reposicao".pedidossituacao p on p.codcolaborador = c.nome where (p.situacaopedido is null or p.situacaopedido ='
                                          + "'Atribuido')"+"and c.situacao  = 'ATIVO' group by c.nome ",conn)
    DistribuicaoColaborador['total_peças'] = DistribuicaoColaborador['total_peças'].replace('', numpy.nan).fillna('')

    return DistribuicaoColaborador

def Distribuicao2(empresa):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'select c.nome, sum(p.qtdepedida)as total_peças from "Reposicao".cadusuarios c left join "Reposicao".pedidossituacao p on p.codcolaborador = c.nome where (p.situacaopedido is null or p.situacaopedido ='+ "'Atribuido')"+"and c.situacao  = 'ATIVO' group by c.nome "
    cur = conn.cursor()
    cur.execute(consulta)
    # Armazena os resultados da consulta em uma matriz
    matriz_resultados = []
    for linha in cur.fetchall():
        matriz_resultados.append(list(linha))
    conn.close()

    return matriz_resultados

x = TabelaRetorna('1')
x = x[x["MARCA"] == 'PACO']
x = x['sugerido'].sum()
#totalRetronaPACO =listas["sugerido"].sum()

    #totalRetronaPACO =listas["sugerido"].sum()
print(x)
# Finaliza a contagem do tempo de execução
#fim = time.perf_counter()

# Calcula o tempo total de execução
#tempo_total = fim - inicio
# Exibe o tempo total de execução
#print(f"O tempo de execução foi de {tempo_total:.6f} segundos.")
#num_linhas = x.shape[0]
#print(num_linhas)






