from src.database.db_phpMySql import get_connection
from src.models.productModel import Product
class ProductService():
    
    @classmethod
    def get_product(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                #cursor.execute('CALL select_all_product();')
                cursor.callproc('select_all_product')
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
                #cursor.execute("INSERT INTO producto (id_producto, nombre_producto,descr_producto, marca_producto, precio_producto, stock_producto) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
                               #.format(id_producto, nombre_producto, descr_producto, marca_producto, precio_producto, stock_producto))
                cursor.callproc('insert_product', (id_producto, nombre_producto, descr_producto, marca_producto, precio_producto, stock_producto))               
                connection.commit()
                #print(cursor)
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)    
            
                
    @classmethod
    def patch_product(cls, producto: Product ):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                id_producto =producto.id_producto
                nombre_producto = producto.nombre_producto
                descr_producto = producto.descr_producto
                marca_producto = producto.marca_producto
                precio_producto = producto.precio_producto
                stock_producto = producto.stock_producto
                
                
                #cursor.execute("UPDATE producto SET nombre_producto = '{0}', descr_producto = '{1}', marca_producto = '{2}', precio_producto = {3}, stock_producto = {4}  WHERE producto.id_producto = {5}".format(nombre_producto,descr_producto,marca_producto,precio_producto,stock_producto,id_producto))
                cursor.callproc('update_product2', (id_producto, nombre_producto, descr_producto, marca_producto, precio_producto, stock_producto)) 
                
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
                #cursor.execute('DELETE FROM producto WHERE producto.id_producto = %s', (id_producto)) Aqui uso SQL
                #cursor.execute("CALL delete_product(%s)", (id_producto)) Aqui uso procedimientos
                cursor.callproc('delete_product', (id_producto,)) # Aqui uso otro metodo callproc para trabajar con procedimientos
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)