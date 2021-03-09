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
    except (Exception, psycopg2.Error) as error:
        print("Impossible de se connecter au serveur postgres : " + str(error))

connect()