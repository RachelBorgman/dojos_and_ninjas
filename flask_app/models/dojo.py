
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.ninjas = []
    @classmethod
    def save (cls, data):
        query = """
            INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_one_dojo(cls, db_data):
        print("data:")
        print(db_data)
        query = """
                SELECT * FROM dojos LEFT OUTER JOIN ninjas ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, db_data)
        print("results:")
        print(results)
        dojo = None
        if int(len(results)) > 0:
            dojo = cls(results[0])
            # if results[0]['ninjas.id'] != 
            for row_from_db in results:
                ninja_data = {
                    "id": row_from_db['ninjas.id'],
                    "first_name": row_from_db['first_name'],
                    "last_name": row_from_db['last_name'],
                    "age": row_from_db['age'],
                    "created_at": row_from_db['created_at'],
                    "updated_at": row_from_db['updated_at'],
                    "dojo_id": row_from_db['dojo_id']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
    
    @classmethod
    def update_dojo(cls,data):
        query = """
            UPDATE dojos
            SET name = %(name)s, updated_at=NOW()
            WHERE id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)