# app/services.py
import requests
import google.generativeai as genai
from flask import current_app
from datetime import datetime, timedelta

def get_nasa_neos():
    """
    Obtiene una lista de Objetos Cercanos a la Tierra (NEOs) desde la API de la NASA.
    """
    api_key = current_app.config['NASA_API_KEY']
    if not api_key:
        return {"error": "NASA API key not configured."}
    
    start_date = datetime.now().strftime('%Y-%m-%d')
    end_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data from NASA API: {e}"}

def get_gemini_analysis(meteorite_data, location):
    """
    Genera un análisis del impacto ambiental usando la API de Gemini.
    """
    api_key = current_app.config['GEMINI_API_KEY']
    if not api_key:
        return "Gemini API key not configured."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        prompt = f"""
        Eres un experto en geología y ciencias ambientales. Tu tarea es analizar el impacto simulado de un meteorito en una ubicación específica.
        
        Datos del Meteorito:
        - Diámetro: {meteorite_data['diameter']:.2f} metros
        - Velocidad de impacto: {meteorite_data['velocity']:.2f} km/s
        - Energía liberada: {meteorite_data['energy']:.2f} megatones de TNT
        - Diámetro del cráter estimado: {meteorite_data['crater_diameter']:.2f} metros

        El meteorito impactará en las siguientes coordenadas geográficas:
        - Latitud: {location['lat']}
        - Longitud: {location['lng']}

        Por favor, proporciona el siguiente análisis en español y en un formato claro:
        1.  **Descripción de la Zona de Impacto:** Describe brevemente el tipo de terreno, geografía y si es una zona poblada, rural, industrial o natural basándote en las coordenadas.
        2.  **Análisis del Daño Ambiental:** Detalla los efectos inmediatos (onda de choque, pulso térmico, terremoto local) y a largo plazo (cambios en el ecosistema, contaminación) que un evento de esta magnitud causaría en esa ubicación.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"