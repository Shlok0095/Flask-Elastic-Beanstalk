from application import application

def test_home_route():
    client = application.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Calculator' in response.data

def test_calculation():
    client = application.test_client()
    response = client.post('/calculate', data={
        'num1': '10',
        'num2': '5',
        'operation': 'add'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 15
