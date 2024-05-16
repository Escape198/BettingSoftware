import pytest
import requests


BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def event_id():
    return "1"


@pytest.fixture
def bet_data(event_id):
    return {"event_id": event_id, "amount": 10.0}


@pytest.fixture
def empty_bets_db():
    # Стартуем с пустой базы данных ставок
    return []


@pytest.fixture
def populated_bets_db(event_id):
    # Предварительно
    return [{"bet_id": 1, "event_id": event_id, "amount": 10.0}, {"bet_id": 2, "event_id": event_id, "amount": 20.0}]


@pytest.fixture
def cleanup():
    yield


def test_create_bet(event_id, bet_data):
    # Отправляем POST запрос для создания ставки
    response = requests.post(f"{BASE_URL}/bets/", json=bet_data)
    assert response.status_code == 200
    assert "bet_id" in response.json()


def test_read_bets_empty(empty_bets_db):
    # Отправляем GET запрос для получения истории
    response = requests.get(f"{BASE_URL}/bets/")
    assert response.status_code == 200

    assert response.json() == {"detail": "No bets available"}


def test_read_bets_populated(populated_bets_db):
    # Отправляем GET запрос для получения истории ставок
    response = requests.get(f"{BASE_URL}/bets/")

    assert response.status_code == 200
    assert len(response.json()) == len(populated_bets_db)


def test_create_bet_missing_event_id(bet_data):
    # Отправляем POST запрос с отсутствующим event_id
    del bet_data["event_id"]
    response = requests.post(f"{BASE_URL}/bets/", json=bet_data)

    assert response.status_code == 422


def test_create_bet_invalid_amount(event_id):
    # Отправляем POST запрос с неверными данными для суммы ставки
    invalid_bet_data = {"event_id": event_id, "amount": -10.0}
    response = requests.post(f"{BASE_URL}/bets/", json=invalid_bet_data)

    assert response.status_code == 422
