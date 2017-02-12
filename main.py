from flask import Flask, request, render_template, jsonify
from sympy import *
from sympy.polys.polyfuncs import interpolate
import numpy as np

print('hi')

x = Symbol('x')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('uk.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    data = request.data.decode("utf-8").split('|')
    x_vals = list(map(lambda x: int(x), data[0].split()))
    y_vals = list(map(lambda x: int(x), data[1].split()))

    i = interpolate(list(zip(x_vals, y_vals)), x)

    x_inter_vals = np.linspace(min(x_vals), max(x_vals), 1000)
    y_inter_vals = lambdify(x, i, 'numpy')(x_inter_vals)

    return jsonify({
        'x': list(x_inter_vals),
        'y': list(y_inter_vals),
        'formula': latex(i)
    })

@app.route('/ua')
def ua():
    return render_template('uk.html')

@app.route('/en')
def en():
    return render_template('en.html')

if __name__  == "__main__":
    app.run()
