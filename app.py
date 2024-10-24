from flask import Flask ,render_template ,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['post'])
def result():
    try:    
        # a=request.form.get("output_button")
        
        if request.method == 'POST':
            num1=request.form.get("num1")
            num2=request.form.get("num2")
            if num1 is None or not num2:
                error="Please enter the values"
                return render_template('home.html',e=error)
            a = request.form.get("output_button")
            num1=float(num1)
            num2=float(num2)
            if a=="add":
                result=f"sum of {num1} and {num2} is {num1+num2}"
                
            elif a=="sub":
                result=f"subtraction of {num1} and {num2} is {num1-num2}"
                
                
            elif a=="mul":
                result=f"Multiplication of {num1} and {num2} is {num1*num2}"
                
                
            elif a=="div":
                result=f"Division of {num1} and {num2} is {num1/num2}"
                
        else:
            result=print("invalid input")
                
        return render_template("home.html",r=result)
    except Exception as e:
        error=str(e)
        return render_template("home.html",e =error)

