from flask import Flask, render_template, request, jsonify
import random

application = Flask(__name__)

# Sample quotes for motivation section
MOTIVATIONAL_QUOTES = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal.",
    "Dream big and dare to fail.",
    "Your only limit is your mind.",
    "Every expert was once a beginner."
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
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
