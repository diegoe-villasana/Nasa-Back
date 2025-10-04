# app/__init__.py (NUEVA VERSIÓN FINAL)

import os
from dotenv import load_dotenv
from flask import Flask

# PASO 1: Pegamos aquí la configuración que copiamos
load_dotenv()

class Config:
    """Clase de configuración para cargar las variables de entorno."""
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# PASO 2: El resto del código ahora usa la clase Config de aquí arriba
def create_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Ahora carga el objeto 'Config' que está definido en este mismo archivo.
    app.config.from_object(Config)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app