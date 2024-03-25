from src.database.db_phpMySql import get_connection

class ProductService():
    
    @classmethod
    def get_product(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM producto')
                result = cursor.fetchall()
                print(result)
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)