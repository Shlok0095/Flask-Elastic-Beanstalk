from application import application
from unittest.mock import patch

def test_home_route():
    with patch('flask.render_template', return_value='Mocked Template'):
        client = application.test_client()
        response = client.get('/')
        assert response.status_code == 200

def test_calculation():
    client = application.test_client()
    # Test addition
    response = client.post('/calculate', data={
        'num1': '10',
        'num2': '5',
        'operation': 'add'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 15

    # Test division by zero
    response = client.post('/calculate', data={
        'num1': '10',
        'num2': '0',
        'operation': 'divide'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
