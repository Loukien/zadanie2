# Użyj obrazu bazowego Pythona
FROM python:3.9


# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki aplikacji do kontenera
COPY . /app

# Zainstaluj wymagane pakiety
RUN pip install --no-cache-dir flask pytz timezonefinder

# Ustaw zmienną środowiskową
ENV PORT=5000

# Otwórz port aplikacji
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]

