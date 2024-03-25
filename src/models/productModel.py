class Product():
    def __init__(self, id_producto, 
                 nombre_producto, 
                 descr_producto, 
                 marca_producto, 
                 precio_producto, 
                 stock_producto) -> None:
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descr_producto = descr_producto
        self.marca_producto = marca_producto
        self.precio_producto = precio_producto 
        self.stock_producto = stock_producto