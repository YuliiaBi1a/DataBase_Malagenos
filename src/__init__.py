from flask import Flask
from .routes import productRouter, providerRouter


app = Flask( __name__ )

def init_app(config):
    app.config.from_object(config)
    
    app.register_blueprint(productRouter.main, url_prefix='/product')
    app.register_blueprint(providerRouter.main, url_prefix='/provider')
    return app