# Simple REST API

Proste REST API zbudowane w FastAPI z trzema endpointami.

## Instalacja

```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
uvicorn main:app --reload
```

API będzie dostępne pod adresem: `http://localhost:8000`

## Endpointy

### 1. GET /health

Zwraca status API i aktualny czas.

```bash
curl http://localhost:8000/health
```

Odpowiedź:
```json
{
  "status": "OK",
  "timestamp": "2024-11-15T10:30:00.123456"
}
```

### 2. GET /items

Zwraca listę wszystkich elementów.

```bash
curl http://localhost:8000/items
```

Odpowiedź:
```json
[
  {
    "id": 1,
    "name": "Element 1",
    "description": "Opis 1"
  },
  {
    "id": 2,
    "name": "Element 2",
    "description": "Opis 2"
  }
]
```

### 3. POST /items

Dodaje nowy element do listy.

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Nowy element", "description": "Nowy opis"}'
```

Odpowiedź:
```json
{
  "id": 3,
  "name": "Nowy element",
  "description": "Nowy opis"
}
```

## Dokumentacja interaktywna

FastAPI automatycznie generuje dokumentację:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
