import psycopg2

class PostgreSQL:

    def __init__(self):
        self.connection = None
        self.id = 0

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
            CREATE TABLE IF NOT EXISTS person(id INT NOT NULL PRIMARY KEY);"""
            cur.execute(sql_create_table)
            self.connection.commit()
            cur.close()
            print("Création de la table réussie")
            return True
        except (Exception, psycopg2.Error) as error:
            print("Impossible de créer la table dans la base postgres : " + str(error))
            return False

    def empty(self):
        try:
            cur = self.connection.cursor()
            sql_exist_id = "SELECT count(*) FROM person;"
            cur.execute(sql_exist_id)
            sql_id = cur.fetchone()
            cur.close()
            if sql_id and type(sql_id)==tuple and sql_id[0] == 0:
                print("la table person est vide")
                return True
            else:
                return False
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'accéder au contenu de la table person : " + str(error))
            return False

    def insert_id(self,id):
        try:
            cur = self.connection.cursor()
            sql_insert_id = "INSERT INTO person(id) VALUES(%s);"
            cur.execute(sql_insert_id %(id))
            self.connection.commit()
            cur.close()
            self.id = id
            print("id inséré : ",self.id)
            return True
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'insérer la valeur de l'id n'existe pas : " + str(error))
            return False        

    def get_id(self):
        try:
            cur = self.connection.cursor()
            sql_id = "SELECT id FROM person;"
            cur.execute(sql_id)
            sql_id = cur.fetchone()
            if sql_id:
                self.id = sql_id[0]
                print("id récupéré : ",self.id)
            else:
                print(sql_id)
            cur.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'accéder à la valeur de l'id : " + str(error))
            return False

    def increment_id(self):
        try:
            self.get_id()
            self.id += 1
            cur = self.connection.cursor()
            sql_update_id = "UPDATE person SET id=%s;"
            cur.execute(sql_update_id %(self.id))
            self.connection.commit()
            cur.close()
            print("id incrémenté : ",self.id)
        except (Exception, psycopg2.Error) as error:
            print("Impossible d'incrémenter à la valeur de l'id : " + str(error))

if __name__=="__main__":
    db = PostgreSQL()
    if db.connect():
        cnt = db.connection
        if db.create_table():
            if db.empty():
                db.insert_id(0)
            else:
                db.increment_id()  