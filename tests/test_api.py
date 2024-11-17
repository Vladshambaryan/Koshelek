import requests


def test_api():

    payload = {}
    headers = {
        'EXCH-SESSION-ID': '4d5fa583-ea79-4c42-af51-e6f820c992c8',
        'sec-ch-ua-platform': '"Windows"',
        'Authorization': 'BC42B11DF8561B4FEEA49BC80F272F9825BCBBFE5A3F70E1CAD24D2111B0A3A8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'host': 'front.koshelek.ru'
    }
    url = "https://koshelek.ru/api/p2p/transfer"
    data = {
        "recipient_card": "4111111111111111",
        "amount": 1,  # Превышение лимита
        "comment": "Тестовый перевод"
    }
    response = requests.post(url, json=data, headers=headers)

    print(response.text)
    # Проверка сообщения об ошибке
    assert response.status_code == 404
