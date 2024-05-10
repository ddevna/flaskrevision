from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal' method = ['GET'])
def math_operator:
    operator=request.json['operation']
    num1=request.json['num1']
    num2=request.json['num2']

    if operation == 'add':
        result=num1+num2

    elif operation == 'subtract':
        result=num1-num2

    elif operation == 'multiply':
        result=num1*num2

    else:
        result=num1/num2
    return result

if __name__ == '__main__':
    app.run()