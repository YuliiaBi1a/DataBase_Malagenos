from flask import Blueprint, request
from src.services.provider_productService import ProviderProductService
from src.models.provider_productModel import Provider_Product
main = Blueprint('provider_product_blueprint', __name__)

@main.route('/', methods = ['GET','POST','PATCH','DELETE'])

def manage_provider():
    if request.method == 'GET':
        get_provider_product = ProviderProductService.get_provider_product()
        print(get_provider_product)
    
    elif request.method  =='POST':
        
        id_provider = request.json['proveedor']['id_proveedor']
        id_product = request.json['producto']['id_producto']
        
        provider_product_table = Provider_Product(None,id_provider,id_product)
        post_provider_product  = ProviderProductService.post_provider_product(provider_product_table)
        print(post_provider_product)
        
    elif request.method == "PATCH": 
        id_proveedor_producto = request.json['id_proveedor_producto']
        updates = request.json['updates']
        patch_provider_product = ProviderProductService.patch_provider_product(id_proveedor_producto, updates)
        print(patch_provider_product) 
    
    elif request.method == "DELETE":
        id_proveedor_producto = request.json['id_proveedor_producto']
        delete_provider_product = ProviderProductService.delete_provider_product(id_proveedor_producto)
        print(delete_provider_product) 
             
    print("Eso veo en la consola")
    return "Eso es tabla proveedor_producto"