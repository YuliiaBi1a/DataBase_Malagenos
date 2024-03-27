from src.database.db_phpMySql import get_connection
from src.models.providerModel import Provider

class ProviderService():
    
    @classmethod
    def get_provider(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM proveedor')
                result = cursor.fetchall()
                print(result)
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)
    
    @classmethod
    def post_provider(cls, provider_table:Provider):
        try:
            connection  = get_connection()
            
            id_proveedor = provider_table.id_proveedor 
            nombre_proveedor =  provider_table.nombre_proveedor
            direccion_proveedor =  provider_table.direccion_proveedor
            telefono_proveedor = provider_table.telefono_proveedor
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO proveedor (id_proveedor, nombre_proveedor, direccion_proveedor, telefono_proveedor) VALUES ('{0}', '{1}', '{2}', '{3}')"
                               .format(id_proveedor,nombre_proveedor,direccion_proveedor,telefono_proveedor))
                connection.commit()
                print("Registro guardado exitosamente")
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)
    
    @classmethod
    def patch_provider(cls, id_proveedor, updates):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                # Створюємо рядок для SQL-запиту для оновлення курсу
                set_clause = ", ".join([f"{key} = '{value}'" for key, value in updates.items()])
                
                # Виконуємо SQL-запит PATCH для оновлення курсу з вказаним ID
                cursor.execute(f'UPDATE proveedor SET {set_clause} WHERE proveedor.id_proveedor = %s', (id_proveedor,))
                
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)
            
    @classmethod
    def delete_provider(cls, id_proveedor): 
        try:
            connection  = get_connection()
            print(connection)
            
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM proveedor WHERE proveedor.id_proveedor = %s', (id_proveedor))
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)