# coding: utf-8
import psycopg2

def connect():
    try:
        host = "local_postgres"
        user = "postgres"
        dbname = "postgres"
        password = "test"
        cnt_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)
        connection = psycopg2.connect(cnt_string)
        print("Connexion réussie : " + str(connection))
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Impossible de se connecter au serveur postgres : " + str(error))
        return None

def create_table():
    cnt = connect()
    if cnt:
        try:
            cur = cnt.cursor()
            sql_create_table = "CREATE TABLE person(id INT NOT NULL PRIMARY KEY)"
            cur.execute(sql_create_table)
            print("Création de la table réussie")
        except (Exception, psycopg2.Error) as error:
            print("Impossible de créer la table dans la base postgres : " + str(error))

create_table()