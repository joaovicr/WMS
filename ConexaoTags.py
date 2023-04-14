import pyodbc
import pandas as pd
import openpyxl


def ConexaoTAGS():
    # Conectado ao Banco DE DADOS do ERP DA EMPRESA VIA ODBC
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')

    db_path = r"C:\Users\Jvictor\pythonProject2\Banco_De_Dados.accdb"
    conn2 = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + db_path + ";")

    df_Tags_Estoque = pd.read_sql("SELECT codBarrasTag, situacao, codNaturezaAtual, codReduzido "
                                                  "FROM tcr.TagBarrasProduto  where codEmpresa = 1 and situacao = 3 and codNaturezaAtual = 5 ", conn)


    df_Banco_de_Dados = pd.read_sql("SELECT top 100 Matricula, Endereco, Codigo_Barras as codBarrasTag, Data_HoraAtualizacao from Banco_De_Dados order by Data_HoraAtualizacao desc  ", conn2)

    df_Banco_de_Dados['codBarrasTag'] = df_Banco_de_Dados['codBarrasTag'].str.slice(stop=-1)

    df_Banco_de_Dados = pd.merge(df_Banco_de_Dados, df_Tags_Estoque, on = 'codBarrasTag', how='left')

    conn.close()
    conn2.close()


    print(df_Tags_Estoque)
    print(df_Banco_de_Dados)
    df_Tags_Estoque.to_excel('TAGS.xlsx', index=False)
    df_Banco_de_Dados.to_excel('Banco de Dados.xlsx', index=False)
    print(df_Banco_de_Dados)