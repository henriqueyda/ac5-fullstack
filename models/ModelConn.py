from app import app
from flask_mysqldb import MySQL

mysql = MySQL(app)


class ClienteModel():

    def cadastrarEmail():
        nome = 'Henrique'
        email = 'aaaa@aaaa.com'
        telefone = '555555555555'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes (nome, email, telefone) VALUES(%s,%s,%s)''',(nome,email,telefone))
        mysql.connection.commit()
        cursor.close()

        return 'Criado com sucesso'
