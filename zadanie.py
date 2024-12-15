from flask import Flask, request
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import logging
import os

# Konfiguracja logowania
logging.basicConfig(filename="server.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info("Uruchomiono serwer. Autor: Kacper Pasturczak")

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Funkcja obsługująca stronę główną
@app.route('/')
def home():
    client_ip = request.remote_addr
    logging.info(f"Połączenie od IP: {client_ip}")

    # Wyznaczenie strefy czasowej na podstawie IP
    tz_finder = TimezoneFinder()
    latitude, longitude = 52.0, 21.0  # Przykładowe dane do testów, tutaj dodać obsługę API do lokalizacji IP
    timezone_str = tz_finder.timezone_at(lat=latitude, lng=longitude)
    if timezone_str:
        local_time = datetime.now(pytz.timezone(timezone_str))
    else:
        timezone_str = "Nieznana"
        local_time = "Nieznana"

    return f"""
    <h1>Twój adres IP: {client_ip}</h1>
    <p>Strefa czasowa: {timezone_str}</p>
    <p>Data i godzina lokalna: {local_time}</p>
    """

# Uruchamianie serwera
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    logging.info(f"Serwer nasłuchuje na porcie: {port}")
    app.run(host="0.0.0.0", port=port)