from src.database.db_phpMySql import get_connection
from src.models.provider_productModel import Provider_Product
from flask import jsonify
class ProviderProductService():
    
    @classmethod
    def get_provider_product(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_proveedor_producto, proveedor.nombre_proveedor, producto.nombre_producto, producto.precio_producto FROM proveedor_producto INNER JOIN proveedor ON proveedor_producto.id_proveedorFK = proveedor.id_proveedor INNER JOIN producto ON proveedor_producto.id_productoFK = producto.id_producto")
                result = cursor.fetchall()
                print(result)
                
            connection.close()
            return jsonify(result)
            #return "Data base is close"
        
        except Exception as ex:
            print(ex)
            return jsonify({"error": "An error occurred"}), 500
    
    @classmethod
    def post_provider_product(cls, provider_table:Provider_Product):
        try:
            connection  = get_connection()
            id_provider_product = provider_table.id_proveedor_producto
            id_provider = provider_table.proveedor 
            id_product =  provider_table.producto
            
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO proveedor_producto (id_proveedor_producto, id_proveedorFK, id_productoFK) VALUES ('{0}', '{1}', '{2}')"
                               .format(id_provider_product,id_provider,id_product))
                connection.commit()
                print("Registro guardado exitosamente")
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)
    
    @classmethod
    def patch_provider_product(cls, id_proveedor_producto, updates):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                # Створюємо рядок для SQL-запиту для оновлення курсу
                set_clause = ", ".join([f"{key} = '{value}'" for key, value in updates.items()])
                
                # Виконуємо SQL-запит PATCH для оновлення курсу з вказаним ID
                cursor.execute(f'UPDATE proveedor_producto SET {set_clause} WHERE proveedor_producto.id_proveedor_producto = %s', (id_proveedor_producto,))
                
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)
            
    @classmethod
    def delete_provider_product(cls, id_proveedor_producto): 
        try:
            connection  = get_connection()
            print(connection)
            
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM proveedor_producto WHERE proveedor_producto.id_proveedor_producto = %s', (id_proveedor_producto))
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)