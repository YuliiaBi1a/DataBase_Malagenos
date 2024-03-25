from flask import Blueprint
from src.services.productService import ProductService

main = Blueprint('mgmalagenos_blueprint', __name__)

@main.route('/')
def manage_product():
    ProductService.get_product()
    print('Esto se imprime en consola')
    return 'Esto se ve en la pagina'