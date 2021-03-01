from mysql.connector import connection
from mysql.connector import Error


def enviar_dados(nome, cpf, email, telefone):
    try:
        con = connection.MySQLConnection(
            host='localhost',
            user='root',
            password= 'root',
            database='tabula'
            )

        cursor = con.cursor()

        query = """INSERT INTO pdf_cadastro (nome, cpf, email, telefone)
                   VALUES ('%s', '%s', '%s', '%s')""" % (nome, cpf, email, telefone)

        cursor.execute(query)
        con.commit()
        cursor.close()
        print('Enviado com sucesso')
    except Exception  as erro:
        print('Falha ao enviar dados: ' + erro)
    #finally:
    #    if (con.is_connected()):
    #        cursor.close()
    #3        con.close()
    #        print('Conexão encerrada com sucesso')
    