from src.database.db_phpMySql import get_connection
from src.models.productModel import Product
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
    
    @classmethod
    def post_product(cls, product_table:Product):
        try:
            connection  = get_connection()
            #print(connection)
            id_producto = product_table.id_producto
            nombre_producto = product_table.nombre_producto
            descr_producto = product_table.descr_producto 
            marca_producto = product_table.marca_producto
            precio_producto = product_table.precio_producto
            stock_producto = product_table.stock_producto
            
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO producto (id_producto, nombre_producto,descr_producto, marca_producto, precio_producto, stock_producto) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
                               .format(id_producto, nombre_producto, descr_producto, marca_producto, precio_producto, stock_producto))
                connection.commit()
                #print(cursor)
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)    
            
                
    @classmethod
    def patch_product(cls, id_producto, updates):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                # Створюємо рядок для SQL-запиту для оновлення курсу
                set_clause = ", ".join([f"{key} = '{value}'" for key, value in updates.items()])
                
                # Виконуємо SQL-запит PATCH для оновлення курсу з вказаним ID
                cursor.execute(f'UPDATE producto SET {set_clause} WHERE producto.id_producto = %s', (id_producto,))
                
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)
            
    @classmethod
    def delete_product(cls, id_producto): 
        try:
            connection  = get_connection()
            print(connection)
            
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM producto WHERE producto.id_producto = %s', (id_producto))
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)