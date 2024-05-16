```bash
docker compose up --build
/
uvicorn myapp.main:app --reload
```
Запуск тестов
```
pytest
```

BetCreate
-
Класс для создания ставки на событие.

Атрибуты:

event_id: идентификатор события (строка или число)
amount: сумма ставки (положительное число с двумя знаками после запятой)

BetResult
-
Класс для представления результата ставки.

Атрибуты:

bet_id: уникальный идентификатор ставки (целое число)
status: статус ставки - "placed", "won", "lost"

API Endpoints
-
POST /bets
Совершает ставку на событие.

Пример тела запроса (JSON):

`
{
  "event_id": "1",
  "amount": 10.0
}
`

---
Переходим :)

http://localhost:8000/docs
