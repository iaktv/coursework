import pytest
from src.utils import change_date_format, change_card, change_account, get_filter_state, get_operation_info


@pytest.fixture
def operation_listed():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]


def test_change_date_format():
    assert change_date_format("2019-06-21T12:34:06.351022") == "21.06.2019"
    assert change_date_format("2018-08-19T04:27:37.904916") == "19.08.2018"
    assert change_date_format("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_change_card():
    assert change_card("MasterCard 9175985085449563") == "MasterCard 9175 98** **** 9563"
    assert change_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert change_card("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert change_card("Maestro 4598300720424501") == "Maestro 4598 30** **** 4501"


def test_change_account():
    assert change_account("Счет 82781399328834147668") == "Счет **7668"
    assert change_account("Счет 14211924144426031657") == "Счет **1657"
    assert change_account("Счет 43597928997568165086") == "Счет **5086"


def test_get_filter_state(operation_listed):
    assert get_filter_state(operation_listed) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]


def test_get_operation_info():
    example = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }
    assert get_operation_info(example) == None

