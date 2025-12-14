# TODO API - Menadżer Zadań

**Autor:** Tim
**Data:** 2024-12-14

## Opis projektu

REST API dla menadżera zadań z zapisem do pliku JSON.

## Technologie

- Python 3.11+
- FastAPI
- JSON (do przechowywania danych)

## Instalacja i uruchomienie

### Wymagania

- Python 3.11+

### Krok po kroku

```bash
# 1. Sklonuj repozytorium
git clone [URL_TWOJEGO_REPO]

# 2. Przejdź do katalogu
cd todo-api

# 3. Zainstaluj zależności
pip install -r requirements.txt

# 4. Uruchom serwer
uvicorn main:app --reload
```

Serwer powinien być dostępny pod adresem: `http://localhost:8000`

## Endpointy API

### 1. GET /health

Opis: Sprawdza status API

Przykład:
```bash
curl http://localhost:8000/health
```

Odpowiedź:
```json
{
  "status": "OK",
  "timestamp": "2024-11-15T10:30:00Z"
}
```

### 2. GET /tasks

Opis: Pobiera wszystkie zadania

Przykład:
```bash
curl http://localhost:8000/tasks
```

Odpowiedź:
```json
[
  {
    "id": 1,
    "title": "Zrobić zakupy",
    "description": "Mleko, chleb, masło",
    "completed": false,
    "createdAt": "2024-11-15T10:00:00Z"
  }
]
```

### 3. POST /tasks

Opis: Dodaje nowe zadanie

Przykład:
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Nowe zadanie","description":"Opis"}'
```

Request body:
```json
{
  "title": "Nowe zadanie",
  "description": "Opis zadania"
}
```

Odpowiedź (201):
```json
{
  "id": 1,
  "title": "Nowe zadanie",
  "description": "Opis zadania",
  "completed": false,
  "createdAt": "2024-11-15T12:00:00Z"
}
```

### 4. PUT /tasks/:id

Opis: Modyfikuje istniejące zadanie

Przykład:
```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Zaktualizowany","completed":true}'
```

Request body:
```json
{
  "title": "Zaktualizowany tytuł",
  "description": "Nowy opis",
  "completed": true
}
```

Odpowiedź (200):
```json
{
  "id": 1,
  "title": "Zaktualizowany tytuł",
  "description": "Nowy opis",
  "completed": true,
  "createdAt": "2024-11-15T10:00:00Z",
  "updatedAt": "2024-11-15T13:00:00Z"
}
```

Odpowiedź przy błędzie (404):
```json
{
  "error": "Task not found",
  "id": 999
}
```

## Testowanie

API przetestowane przy użyciu curl oraz automatycznej dokumentacji FastAPI dostępnej pod:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Struktura projektu

```
todo-api/
├── main.py
├── tasks.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Napotkane problemy i rozwiązania

Brak - implementacja przebiegła bez problemów.
