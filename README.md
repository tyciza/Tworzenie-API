# Tworzenie API we Flask'u
Ten projekt zawiera kilka wersji prostego API stworzonego przy użyciu Flask. API udostępnia różne endpointy, w tym:

- Strona główna (`/`)
- Statyczna podstrona (`/mojastrona`)
- Endpoint z parametrem (`/hello?name=TwojeImie`)
- Endpoint do predykcji (`/api/v1.0/predict?num1=...&num2=...`)

## Zawartość

- `app1.py` – podstawowa wersja z jednym endpointem
- `app2.py` – dodana podstrona
- `app3.py` – obsługa parametru `name` w `/hello`
- `app.py` – pełna wersja z prostym modelem predykcyjnym
- `requirements.txt` – wymagane biblioteki (Flask)
- `Dockerfile` – konfiguracja Docker
- `README.md` 

## Jak uruchomić


1. Zainstaluj wymagane biblioteki:
    ```bash
    pip install -r requirements.txt
    ```

2. Uruchom aplikację:
    ```bash
    python app.py
    ```
