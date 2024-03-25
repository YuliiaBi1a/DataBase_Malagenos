from flask import Flask
from .routes import productRouter

app = Flask( __name__ )

def init_app(config):
    app.config.from_object(config)
    
    app.register_blueprint(productRouter.main, url_prefix='/product')
    
    return app