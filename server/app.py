from flask import Flask

app = Flask(__name__)

# 1. Index View
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print String View
@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)  # 
    return f"{string_param}"  

# 3. Count View
# 3. Count View
@app.route('/count/<int:num>')
def count(num):
    result = ""
    for i in range(num):
        result += f"{i}\n"  
    return result

# 4. Math View
@app.route('/math/<int:num1>/<operation>/<int:num2>')
# 4. Math View
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    # The test expects ONLY the result, converted to a string
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)