import pymysql

def get_connection():
    try:
        return pymysql.connect ( 
            host = 'localhost',
            database = 'mgmalagenos',
            user = 'root',
            passwd = ''
        )
        
    except Exception as ex:
        print("Error connecting to database: ", str(ex))