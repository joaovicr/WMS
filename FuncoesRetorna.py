import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyodbc
import pandas as pd
import locale
import numpy
from datetime import datetime, timedelta

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # DEFININDO O PADRÃO DOS DADOS PARA APLICAR A FUNCAO LOCALE
def TabelaRetorna(empresa):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    Retorna = pd.read_sql("SELECT codEmpresa, codPedido, vlrSugestao, situacaoSugestao, dataHoraListagem, CONVERT(int,SUBSTRING(dataHoraListagem,1,5)) as DataGeracao "
                          "from ped.SugestaoPed WHERE dataHoraListagem > 0 and codEmpresa in (" + empresa + ") and situacaoSugestao =2 ",
                          conn)

    df_Pedidos = pd.read_sql("SELECT top 100000 codColecao  ,codPedido, codTipoNota, dataPrevFat, codCliente, codRepresentante,"
                            "descricaoCondVenda, vlrPedido as vlrSaldo,qtdPecasFaturadas FROM Ped.Pedido where codEmpresa in (" + empresa + ") order by codPedido desc ",conn)


    RetornaItens = pd.read_sql(
        "Select codPedido, "
        "(SELECT codItemPai  from cgi.Item2 i WHERE i.Empresa = 1 and i.codItem = ps.produto) as codProduto, "
        "SUM(qtdeSugerida) as sugerido , SUM(qtdePecasConf) as conferido  from ped.SugestaoPedItem ps "
        "WHERE codEmpresa in (" + empresa + ") GROUP by codPedido", conn)

    RetornaItens = RetornaItens[RetornaItens['conferido'] == 0]
    Retorna = pd.merge(RetornaItens, Retorna, on='codPedido')
    Retorna = pd.merge(Retorna, df_Pedidos, on='codPedido', how='left')

    Retorna = Retorna.sort_values(by='codCliente')  # escolher como deseja classificar
    Retorna["sugerido"] = Retorna["sugerido"].astype(int)
    Retorna['MARCA'] = Retorna['codProduto'].apply(lambda x: x[:3])
    Retorna['MARCA'] = numpy.where((Retorna['codProduto'].str[:3] == '102') | (Retorna['codProduto'].str[:3] == '202') , 'M.POLLO', 'PACO')
    Retorna['DataGeracao'] = pd.to_datetime(Retorna['DataGeracao'] , origin='1840-12-31', unit='D')
    Retorna = Retorna.sort_values(by='DataGeracao')  # escolher como deseja classificar
    Retorna['DataGeracao']=  Retorna['DataGeracao'].dt.strftime('%d/%m/%Y')
    Retorna = Retorna.reindex()
    Retorna = Retorna.reset_index(drop=True) # adicionando essa linha para resetar o índice
    conn.close()
    return Retorna


x = TabelaRetorna("1")

print(x["DataGeracao"])


