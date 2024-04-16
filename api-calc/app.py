from chalice import Chalice

app = Chalice(app_name='api-calc')


@app.route('/calc/{value1}/{value2}/{operation}', methods=['GET'])
def calculate(value1, value2, operation):
    result = None
    if operation == 'add':
        result = float(value1) + float(value2)
    elif operation == 'subtract':
        result = float(value1) - float(value2)
    elif operation == 'multiply':
        result = float(value1) * float(value2)
    elif operation == 'divide':
        result = float(value1) / float(value2)
    else:
        return {'error': 'Invalid operation. Supported operations: add, subtract, multiply, divide'}

    return {'result': result}
