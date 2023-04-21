import psycopg2

def Funcao_Inserir (Usuario, Codigo_Barras, CodReduzido, Endereco, Engenharia, DataAtualizacao, EngenhariaPai, Descricao):

    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")

    cursor =conn.cursor()

    sql= 'INSERT INTO "Reposicao"."Estoque" ("Usuario", "Codigo_Barras", "CodReduzido", "Endereco", "Engenharia", "DataAtualizacao", "EngenhariaPai","Descricao") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    VALORES = (Usuario, Codigo_Barras, CodReduzido, Endereco, Engenharia, DataAtualizacao, EngenhariaPai,Descricao)
    cursor.execute(sql, VALORES)
    conn.commit()
    cursor.close()

    conn.close()
    # return Funcao_Inserir



#Funcao_Inserir("Luis", "100", "123456", "01-01-01","1045000", "24/03/2023",'z','z')




def Funcao_Inserir_Usuarios (Codigo, Nome, Senha, Situacao, Funcao):

    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")

    cursor =conn.cursor()

    sql= 'INSERT INTO "Reposicao"."cadusuarios" ("codigo", "nome", "senha", "situacao", "funcao") VALUES (%s, %s, %s, %s, %s)'
    VALORES = (Codigo, Nome, Senha, Situacao, Funcao)
    cursor.execute(sql, VALORES)
    conn.commit()
    cursor.close()

    conn.close()
    # return Funcao_Inserir



#Funcao_Inserir_Usuarios(2, "João Victor", "Master100", "ATIVO")

def Funcao_Atualizar_Usuarios (Codigo, Nome, Senha, Situacao, Funcao):

    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")

    cursor =conn.cursor()

    sql= 'UPDATE "Reposicao".cadusuarios SET nome= %s, senha= %s, situacao= %s, funcao= %s where codigo= %s ;'
    VALORES = (Nome, Senha, Situacao, Funcao, Codigo)
    cursor.execute(sql, VALORES)
    conn.commit()
    cursor.close()

    conn.close()
    #return Funcao_Inserir

#Funcao_Atualizar_Usuarios(200, "GRASIELLE", "M", "INATIVO", "COLABORADOR")


def pesquisarPedido(Pedido):
    conn = psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms",
                            password="Master100")
    consulta = 'select * from "Reposicao".pedidossituacao p where "codPedido" = %s '
    valor = (Pedido,)
    cursor = conn.cursor()
    cursor.execute(consulta, valor)

    resultado = cursor.fetchone()
    conn.close()
    return resultado[0]


def AtribuirPedido (Pedido, codcolaborador,qtdpedida):

    conn =psycopg2.connect( host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")
    try:
        pesquisarPedido(Pedido)
        UpdateAtribuicao(Pedido, codcolaborador)


    except:
        cursor =conn.cursor()
        sql = 'INSERT INTO "Reposicao"."pedidossituacao" ("codPedido", "codcolaborador","situacaopedido","qtdepedida") VALUES (%s, %s,%s,%s)'
        VALORES = (Pedido, codcolaborador,'Atribuido',int(qtdpedida))
        cursor.execute(sql, VALORES)
        conn.commit()
        cursor.close()

        conn.close()

def UpdateAtribuicao(Pedido, colaborador):
    conn = psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms",
                            password="Master100")
    cursor = conn.cursor()

    sql = 'UPDATE "Reposicao".pedidossituacao SET codcolaborador= %s WHERE "codPedido"= %s'
    VALORES = (colaborador, Pedido)
    cursor.execute(sql, VALORES)
    conn.commit()
    cursor.close()

    conn.close()



AtribuirPedido('302747', 'teste',1)




