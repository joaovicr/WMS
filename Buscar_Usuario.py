import pyodbc


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