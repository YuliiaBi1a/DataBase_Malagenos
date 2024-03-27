from flask import Blueprint, request
from src.services.providerService import ProviderService
from src.models.providerModel import Provider

main = Blueprint('provider_blueprint', __name__)

@main.route('/', methods = ['GET','POST','PATCH','DELETE'])

def manage_provider():
    
    if request.method == 'GET':  
        get_provider = ProviderService.get_provider()
        print(get_provider)
    
    elif request.method == "POST": 
        nombre_proveedor = request.json['nombre_proveedor']
        direccion_proveedor = request.json['direccion_proveedor'] 
        telefono_proveedor = request.json['telefono_proveedor']
        
        provider_table = Provider(0,nombre_proveedor,direccion_proveedor,telefono_proveedor)

        post_provider = ProviderService.post_provider(provider_table)
        print(post_provider)
    
    elif request.method == "PATCH": 
        id_proveedor = request.json['id_proveedor']
        updates = request.json['updates']
        patch_provider = ProviderService.patch_provider(id_proveedor, updates)
        print(patch_provider) 
    
    elif request.method == "DELETE":
        id_proveedor = request.json['id_proveedor']
        delete_provider = ProviderService.delete_provider(id_proveedor)
        print(delete_provider)  
        
    print("Eso veo en la consola")
    return "Hola proveedor"