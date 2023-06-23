from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for n in results:
            ninjas.append(cls(n))
        return ninjas
    
    @classmethod
    def get_one_ninjas(cls, data):
        query = """
                SELECT * FROM ninjas
                WHERE id = %(id)s;
        """
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update_ninja(cls,data):
        query = """
            UPDATE ninjas
            SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at=NOW()
            WHERE id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    
    # @classmethod
    # def delete_ninja_from_dojo(cls, data):
    #     query = "DELETE FROM ninjas WHERE dojo_id = %(dojo_id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    #     return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id ) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(),%(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)