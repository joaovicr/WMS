import pyodbc
import psycopg2

#FUNCAO PARA PESQUISAR A DESCRIÇÃO DO ITEM NO CSW
def Descricoes(Reduzido):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    consulta = 'SELECT nome FROM cgi.Item  WHERE  codigo = ?'
    valor = (Reduzido)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row.nome])
        resultados = str(resultados[0][0])
    print(resultados)

    conn.close()
    return resultados


#Descricoes('194998')

#FUNÇÃO PARA PESQUISAR O REDUZIDO PARA INSERIR NA TELA DE REPOSIÇÃO
def Pesquisa_Reduzido(TAG):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    consulta = 'SELECT codReduzido FROM tcr.TagBarrasProduto  WHERE codEmpresa = 1 and situacao = 3 and codNaturezaAtual = 5 AND codBarrasTag = ?'
    valor = (TAG)
    cursor = conn.cursor()
    cursor.execute(consulta,valor)
    resultados = []

    for row in cursor:
        resultados.append([row.codReduzido])
        resultados = str(resultados[0][0])
    print(resultados)

    conn.close()
    return resultados


#Pesquisa_Reduzido('01000019499801007373')

#FUNÇÃO PARA PESQUISAR A ENGENHARIA COM TAMANHO E COR PARA INSERIR NA TELA DE REPOSIÇÃO
def Pesquisa_Engenharia(Reduzido):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    consulta = 'SELECT codItemPai || "." || codSeqTamanho || "." || codcor as ENGENHARIA from cgi.Item2  WHERE Empresa = 1 AND codItem = ?'
    valor = (Reduzido)
    cursor = conn.cursor()
    cursor.execute(consulta,valor)
    resultados = []

    for row in cursor:
        resultados.append([row.ENGENHARIA])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados

#Pesquisa_Engenharia('194998')


#FUNÇÃO PARA PESQUISAR A ENGENHARIA PAI PARA INSERIR NA TELA DE REPOSIÇÃO
def Pesquisa_EngenhariaPai(TAG):
    conn = pyodbc.connect(dsn='SISTEMAS CSW', user='root', password='ccscache')
    consulta = 'SELECT SUBSTRING (codEngenharia,2,8) as Engenharia FROM tcr.TagBarrasProduto  WHERE codEmpresa = 1 and situacao = 3 and codNaturezaAtual = 5 AND codBarrasTag = ?'
    valor = (TAG)
    cursor = conn.cursor()
    cursor.execute(consulta,valor)
    resultados = []

    for row in cursor:
        resultados.append([row.Engenharia])
        resultados = str(resultados[0][0])
    print(resultados)

    conn.close()
    return resultados


Pesquisa_EngenhariaPai('01000019499801007268')



#FUNÇÃO PARA PESQUISAR O ENDEREÇO PELO REDUZIDO PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Endereco_Reduzido(Reduzido):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao" from "Reposicao"."Estoque"  WHERE "CodReduzido" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[0]])
        #resultados = str(resultados[0][0])
    print("pesquisar endereco pelo reduzido: " )
    print(resultados )

    conn.close()

    return resultados


#Pesquisa_Endereco_Reduzido('194998')


#FUNÇÃO PARA PESQUISAR O ENDEREÇO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Endereco_Engenharia(Reduzido):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao" from "Reposicao"."Estoque"  WHERE "EngenhariaPai" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[0]])
        #resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Endereco_Engenharia('01000019500502025572')



#FUNÇÃO PARA PESQUISAR A ENGENHARIA PELO REDUZIDO PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Engenharia_Reduzido(Reduzido):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao" from "Reposicao"."Estoque"  WHERE "CodReduzido" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[1]])
        #resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Engenharia_Reduzido('01000019500502025572')


#FUNÇÃO PARA PESQUISAR A ENGENHARIA PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Engenharia_Engenharia(Reduzido):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao" from "Reposicao"."Estoque"  WHERE "EngenhariaPai" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[1]])
       # resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Engenharia_Engenharia('01000019500502025572')





#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELO REDUZIDO PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Descricao_Reduzido(Reduzido):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao" from "Reposicao"."Estoque"  WHERE "CodReduzido" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[2]])
        #resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Descricao_Reduzido('01000019500502025572')


#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Descricao_Engenharia(Reduzido):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Endereco", "Engenharia", "Descricao"  from "Reposicao"."Estoque"  WHERE "EngenhariaPai" = %s'
    valor = (Reduzido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[2]])
       # resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Descricao_Engenharia('01000019500502025572')


#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Quantidade_NoEndereco(Endereco):
    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'select "Endereco",count("Engenharia") as "QuantidadePeca" from "Reposicao"."Estoque" where "Endereco" = %s group by "Endereco"'
    valor = (Endereco,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[1]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#Pesquisa_Quantidade_NoEndereco('10-10-10')


#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_Reduzido_TAG(TAG):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "CodReduzido"  from "Reposicao"."Estoque"  WHERE "Endereco" = %s'
    valor = (TAG,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:

        resultados.append([row[0]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados


#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def Pesquisa_TAG(TAG):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT distinct "Codigo_Barras"  from "Reposicao"."Estoque"  WHERE "Codigo_Barras" = %s'
    valor = (TAG,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[0]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados



#Pesquisa_TAG('01000019500502026926')






#FUNÇÃO PARA PESQUISAR A DESCRIÇÃO PELA ENGENHARIA PARA INSERIR NA TELA DE CONSULTAR ENDEREÇOS
def PesquisaNomeColaborador(codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao"  from "Reposicao"."cadusuarios"  WHERE "codigo" = %s'
    valor = (codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[1]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados

#PesquisaNomeColaborador(1)


def PesquisaSenhaColaborador(codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao"  from "Reposicao"."cadusuarios"  WHERE "codigo" = %s'
    valor = (codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[2]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados



#PesquisaSenhaColaborador(2)


def PesquisaSituacaoColaborador(codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao"  from "Reposicao"."cadusuarios"  WHERE "codigo" = %s'
    valor = (codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[3]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()


    return resultados



#PesquisaSituacaoColaborador(1)

def PesquisasFuncaoColaborador(codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao", "funcao"  from "Reposicao"."cadusuarios"  WHERE "codigo" = %s'
    valor = (codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[4]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()


    return resultados



#PesquisaSituacaoColaborador(1)

def PesquisaNomeColaboradorAtivo(situacao, codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao"  from "Reposicao"."cadusuarios"  WHERE "situacao" = %s and "codigo" = %s'
    valor = (situacao, codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[0]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados

#PesquisaNomeColaboradorAtivo("ATIVO", 1)

def PesquisaSenhaColaborador2(situacao, codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao"  from "Reposicao"."cadusuarios"  WHERE "situacao" = %s and "codigo" = %s'
    valor = (situacao, codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[2]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados

#PesquisaNomeColaboradorAtivo("ATIVO", 1)

def PesquisaPermissaoColaborador(situacao, codigo):
    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    consulta = 'SELECT "codigo", "nome", "senha", "situacao", "funcao"  from "Reposicao"."cadusuarios"  WHERE "situacao" = %s and "codigo" = %s'
    valor = (situacao, codigo,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)
    resultados = []

    for row in cursor:
        resultados.append([row[4]])
        resultados = str(resultados[0][0])
    print(resultados)
    conn.close()

    return resultados

#PesquisaNomeColaboradorAtivo("ATIVO", 1)




