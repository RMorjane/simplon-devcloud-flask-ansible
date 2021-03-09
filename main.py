import psycopg2

class PostgreSQL:

    def __init__(self):
        self.connection = None
        self.id = 1

    def connect(self):
        try:
            host = "local_postgres"
            user = "postgres"
            dbname = "postgres"
            password = "test"
            cnt_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)
            self.connection = psycopg2.connect(cnt_string)
            print("Connexion réussie : " + str(self.connection))
            return True
        except (Exception, psycopg2.Error) as error:
            print("Impossible de se connecter au serveur postgres : " + str(error))
            return False

    def create_table(self):
        try:
            cur = self.connection.cursor()
            sql_create_table = """
            DROP TABLE IF EXISTS person;
            CREATE TABLE IF NOT EXISTS person(id INT NOT NULL PRIMARY KEY);
            INSERT INTO person(id) VALUES(0);"""
            cur.execute(sql_create_table)
            self.connection.commit()
            cur.close()
            print("Création de la table réussie")
            return True
        except (Exception, psycopg2.Error) as error:
            print("Impossible de créer la table dans la base postgres : " + str(error))
            return False

    def getid(self):
        try:
            cur = self.connection.cursor()
            sql_id = "SELECT id FROM person;"
            cur.execute(sql_id)
            self.id = cur.fetchone()[0]
            cur.close()
            print("id : ",self.id)
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'accéder à la valeur de l'id : " + str(error))

if __name__=="__main__":
    db = PostgreSQL()
    if db.connect():
        cnt = db.connection
        if db.create_table():
            db.getid()
            id = db.id        