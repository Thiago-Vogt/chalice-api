import requests

url = 'https://d06a9xo5p0.execute-api.us-east-1.amazonaws.com/api/calc/'

def calculate(value1, value2, operation):
    response = requests.get(url + f'{value1}/{value2}/{operation}')
    if response.status_code == 200:
        result = response.json().get('result')
        return result
    else:
        error = response.json().get('error', 'Unknown error')
        return f'Error: {error}'

# Solicitar entrada do usuário
value1 = input('Digite o primeiro valor: ')
value2 = input('Digite o segundo valor: ')
operation = input('Digite a operação (add, subtract, multiply, divide): ')

# Calcular e exibir resultado
result = calculate(value1, value2, operation)
print(f'O resultado da operação é: {result}')
