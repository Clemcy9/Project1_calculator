from flask import Flask, redirect, render_template, url_for,request


app = Flask(__name__)


# addition function
def add(a,b):
    return a+b

# subtraction function
def sub(a,b):
    return a-b

# divide function
def div(a,b):
    return a/b

# multiply function
def multi(a,b):
    return a*b

# power function
def power(a,b):
    return a**b

# result =0
postion =0
num1 =0
num2 =0

@app.route('/', methods=['GET','POST'])
def index():
    result =0
    if request.method == 'POST':
        data = request.form['screen']
        if(data.find('+') != -1):
            position = data.find('+')
            print('position=:',position)
            num1=float(data[0:position])
            print('this is first value: ',num1)
            num2=float(data[position:len(data)])
            print('this is second value: ',num2)
            result=add(num1,num2)
        elif(data.find('-') != -1):
            position = data.find('-')
            print('position=:',position)
            num1=float(data[0:position])
            print('this is first value: ',num1)
            num2=float(data[position+1:len(data)])
            print('this is second value: ',num2)
            result=sub(num1,num2)
        elif(data.find('*') != -1):
            position = data.find('*')
            print('position=:',position)
            num1=float(data[0:position])
            print('this is first value: ',num1)
            num2=float(data[position+1:len(data)])
            print('this is second value: ',num2)
            result=multi(num1,num2)
        elif(data.find('/') != -1):
            position = data.find('/')
            print('position=:',position)
            num1=float(data[0:position])
            print('this is first value: ',num1)
            num2=float(data[position+1:len(data)])
            print('this is second value: ',num2)
            result=div(num1,num2)
        elif(data.find('^') != -1):
            position = data.find('^')
            print('position=:',position)
            num1=float(data[0:position])
            print('this is first value: ',num1)
            num2=float(data[position+1:len(data)])
            print('this is second value: ',num2)
            result=power(num1,num2)

        return render_template('calculator.html',result=result)
    result =0
    return render_template('calculator.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)