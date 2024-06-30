#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter <= 0:
        return 'Please enter a positive integer'
    
    output = "\n".join(str(x) for x in range(1, parameter + 1)) 
    return output

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    operations = {
      "+": lambda a, b: a + b,
      "-": lambda a, b: a - b,
      "*": lambda a, b: a * b,
      "div": lambda a, b: a / b, 
      "%": lambda a, b: a % b,
  }
    
    try:
        result = operations[operation](int(num1), int(num2))
        return f"{result}"
    except ZeroDivisionError:
        return "Error: Division by zero"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
