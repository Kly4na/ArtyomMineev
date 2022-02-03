
import flask
from gcdmodule import gcd
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/',methods=['POST','GET'])

def calculate():
    ans=''
    if request.method=='POST' and 'number1' in request.form and 'number2' in request.form:
        number_1=float(request.form.get('number1'))
        number_2=float(request.form.get('number2'))
        ans=gcd(number_1,number_2)
    
    return render_template('gcd.html',ans=ans)
    


if __name__ == '__main__':
   app.run(debug = True)
