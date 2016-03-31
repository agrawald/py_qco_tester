from qco.testing.rest_invoker import get


def place_cco_bet():
    offer = get('http://localhost:8080/cashout/bet', [])
