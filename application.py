from flask import Flask, render_template, request, jsonify
import random

application = Flask(__name__)

# Sample quotes for motivation section
MOTIVATIONAL_QUOTES = [
    
]

@application.route('/')
def home():
    quote = random.choice(MOTIVATIONAL_QUOTES)
    return render_template('index.html', quote=quote)

@application.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'})
        
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid number input'})
    except KeyError:
        return jsonify({'error': 'Missing input parameters'})

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
