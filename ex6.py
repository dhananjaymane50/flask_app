from flask import Flask,request

app=Flask(__name__)  # app instance

@app.route('/',methods=['GET'])
def home():
    return('Hello world')
    
@app.route('/add1',methods=['POST'])
def add1():
    a=10
    b=20
    return(f'the addition of {a} and is: {a+b}')

@app.route('/add2/<a>/<b>',methods=['GET'])
def add2(a,b):
    return(f'the addition of {a} and is: {a+b}')
@app.route('/add3<int:a>/<int:b>',methods=['POST'])
def add3(a,b):
    return(f'the addition of {a} and is: {a+b}')
@app.route('/add4',methods=['GET'])
def add4():
    a=request.args.get('number1',default=0,type=int)
    b=request.args.get('number2',default=0,type=int)
    return(f'the addition of {a} and {b} is: {a+b}')
    
if __name__=="__main__":
    app.run(debug=True)