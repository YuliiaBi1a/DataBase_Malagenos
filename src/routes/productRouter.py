from flask import Blueprint,  request
from src.services.productService import ProductService
from src.models.productModel import Product

main = Blueprint('mgmalagenos_blueprint', __name__)

@main.route('/', methods = ['GET','POST','PATCH','DELETE'])
def manage_product():
    
    if request.method == "GET":
        get_product = ProductService.get_product()
        print(get_product)
    
    elif request.method == "POST":
        nombre_producto = request.json['nombre_producto']
        descr_producto = request.json['descr_producto']
        marca_producto = request.json['marca_producto']
        precio_producto = request.json['precio_producto']
        stock_producto = request.json['stock_producto']   
        
        product_table = Product(0,nombre_producto,
                                descr_producto, 
                                marca_producto,
                                precio_producto,
                                stock_producto)
        post_product = ProductService.post_product(product_table)
        print(post_product)
        
        
    elif request.method == "PATCH": 
        id_producto = request.json['id_producto']
        updates = request.json['updates']
        patch_product = ProductService.patch_product(id_producto, updates)
        print(patch_product) 
    
    elif request.method == "DELETE":
        id_producto = request.json['id_producto']
        delete_product = ProductService.delete_product(id_producto)
        print(delete_product)  
           
    print('Esto se imprime en consola')
    return 'Esto se ve en la pagina'