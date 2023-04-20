import psycopg2

def Funcao_Remover (Endereco):

    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")

    cursor =conn.cursor()

    cursor.execute ('DELETE FROM "Reposicao"."Estoque" WHERE "Endereco" = %s',(Endereco,))


    conn.commit()
    cursor.close()
    conn.close()
    return Funcao_Remover


def Funcao_Remover_tag (tag):

    conn =psycopg2.connect(host="wmsbd.cyiuowfro4wv.sa-east-1.rds.amazonaws.com", database="wms_bd", user="wms", password="Master100")

    cursor =conn.cursor()

    cursor.execute ('DELETE FROM "Reposicao"."Estoque" WHERE "Codigo_Barras" = %s',(tag,))


    conn.commit()
    cursor.close()
    conn.close()
    return Funcao_Remover_tag



Funcao_Remover_tag("01000019500502026926")