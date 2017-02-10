from flask import Flask, request, render_template
from sympy import *
from sympy.polys.polyfuncs import interpolate
import numpy as np

x = Symbol('x')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('points.html')

# @app.route("/number/<num>")
# def green(num):
#     l, u = list(map(lambda x: int(x), num.split('-')))
#     # print(color)
#     return str(integrate(x**2, (x, l, u)))

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        # res = request.form
        # jsonData = request.get_json()
        x_vals = list(map(lambda x: int(x), request.form['x'].split()))
        y_vals = list(map(lambda y: int(y), request.form['y'].split()))
        print(x_vals)
        print(y_vals)
        i = interpolate(list(zip(x_vals, y_vals)), x)
        print(latex(i))
        x_inter_vals = np.linspace(min(x_vals), max(x_vals), 1000)
        y_inter_vals = lambdify(x, i, 'numpy')(x_inter_vals)

        return render_template("result.html",
                    data=[list(x_inter_vals), list(y_inter_vals), x_vals, y_vals, latex(i), x_vals, y_vals])


if __name__  == "__main__":
    app.run()
