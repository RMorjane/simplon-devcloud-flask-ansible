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

def create_table(connection):
    try:
        cur = connection.cursor()
        sql_create_table = """
        DROP TABLE IF EXISTS person;
        CREATE TABLE person(id INT NOT NULL PRIMARY KEY);"""
        cur.execute(sql_create_table)
        connection.commit()
        cur.close()
        print("Création de la table réussie")
        return True
    except (Exception, psycopg2.Error) as error:
        print("Impossible de créer la table dans la base postgres : " + str(error))
        return False

def create_id(id):
    cnt = connect()
    if cnt:
        try:
            cur = cnt.cursor()
            sql_create_id = "INSERT INTO person(id) VALUES(%s);"
            cur.execute(sql_create_id %(id))
            cnt.commit()
            cur.close()
            print("Insertion réussie id : ",id)
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'insérrer l'id dans la table person de la base postgres : " + str(error))

cnt = connect()
if cnt and create_table(cnt):
    create_id(1)