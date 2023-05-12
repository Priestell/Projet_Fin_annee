from flask import Flask, render_template, request
from joblib import load
import sklearn
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
import numpy as np
reg = load("./modele/regressor.joblib")
lasso = load("./modele/lasso.joblib")
rf = load("./modele/rf.joblib")
ridge = load("./modele/ridge.joblib")
tree = load("./modele/tree.joblib")
ada = load("./modele/ada.joblib")
knn = load("./modele/knn.joblib")
poly = load("./modele/poly.joblib")
"""Rome : 7
Amsterdam : 1
Barcelona : 2
Dublin : 3
London : 4
Madrid : 5
Munich : 6"""
@app.route('/')
def hello_world():  # put application's code here
    return render_template("main.html")

@app.route('/process-form', methods=['POST'])
def test():
    nom = request.form['nom']
    note = int(request.form['note'])
    ville = int(request.form.get('Ville'))
    piscine = int(request.form.get('piscine'))
    bar = int(request.form.get('bar'))
    dejeuner = int(request.form.get('dejeuner'))
    salle = int(request.form.get('salle'))
    wifi = int(request.form.get('wifi'))
    parking = int(request.form.get('parking'))
    restaurant = int(request.form.get("restaurant"))
    array = np.array([note, wifi, bar, salle, parking, dejeuner, restaurant, piscine, ville])
    array_2d = array.reshape(1, 9)
    var1 = rf.predict(array_2d)
    var2 = ridge.predict(array_2d)
    var3 = tree.predict(array_2d)
    var4 = lasso.predict(array_2d)
    var5 = ada.predict(array_2d)
    var6= knn.predict(array_2d)

    x_poly = poly.fit_transform(array_2d)
    var7 = reg.predict(x_poly)
    return render_template("index.html", var1=var1, var2=var2, var3=var3, var4= var4, var5=var5, var6=var6, var7=var7)

if __name__ == '__main__':
    app.run()