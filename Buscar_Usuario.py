import psycopg2
import pyodbc
import pandas as pd
def Pesquisa_Nome(matricula):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    consulta = 'SELECT * FROM Escala.OperadorEsc WHERE Config =1 AND codOperador = ?'
    valor = (matricula)
    cursor = conn.cursor()
    cursor.execute(consulta,valor)
    resultados = []

    for row in cursor:
        resultados.append([row.nome])
        resultados = str(resultados[0][0])
    print(resultados)


    conn.close()
    return resultados

#Pesquisa_Nome(1414)
def PesquisaTodosUsuaios():
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    Colaboradores = pd.read_sql('select * from "Reposicao".cadusuarios c',
                          conn)

    Colaboradores = Colaboradores[Colaboradores['situacao'] == 'ATIVO']

    Colaboradores = Colaboradores.reindex()
    Colaboradores = Colaboradores.reset_index(drop=True) # adicionando essa linha para resetar o índice
    conn.close()
    return Colaboradores


x = PesquisaTodosUsuaios()
print(x)