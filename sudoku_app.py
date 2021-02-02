# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:37:40 2020

@author: Arijit
"""
"""
from flask import Flask, jsonify
from sudoku import *

sample=np.array([[5,np.nan,np.nan,np.nan,7,np.nan,np.nan,1,np.nan],[np.nan,np.nan,4,np.nan,np.nan,6,np.nan,np.nan,9],[7,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,6,np.nan],
                 [6,np.nan,np.nan,9,5,np.nan,np.nan,np.nan,np.nan],[np.nan,5,2,6,4,8,np.nan,np.nan,np.nan],[8,np.nan,np.nan,3,np.nan,np.nan,np.nan,np.nan,np.nan],
                 [2,np.nan,5,8,np.nan,np.nan,np.nan,4,np.nan],[1,np.nan,8,np.nan,np.nan,np.nan,np.nan,np.nan,7],[np.nan,9,np.nan,np.nan,np.nan,np.nan,2,5,np.nan]
                 ])

k=solver(sample)
ko= {'{} row'.format(i+1): k[i].tolist() for i in range(9)}

app= Flask(__name__)

@app.route('/')

def home():
    return jsonify(ko)

app.run(port= 2000)
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
from sudoku import *
from tabulate import tabulate
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    names= ["cell-{}".format(i) for i in range(81)]
    k=[]
    for name in names:
        val=request.form[name]
        if val == str(0):
            k.append(np.nan)
        elif val == '':
            k.append(np.nan)
        else:
            k.append(int(val))
    sample = np.array(k).reshape(9,9)
    prediction = solver(sample)
    """
    prediction_text = tabulate(prediction, tablefmt='html')
    with open("templates/results.html") as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt)
    body=soup.find('body')
    body.string.replace_with(prediction_text)
    with open("templates/results.html", "w") as outf:
        outf.write(str(soup))
        """
    return render_template('results.html', 
                           zeze=str(prediction[0][0]),zeon=str(prediction[0][1]),zetw=str(prediction[0][2]),zeth=str(prediction[0][3]),zefo=str(prediction[0][4]),zefi=str(prediction[0][5]),zesi=str(prediction[0][6]),zese=str(prediction[0][7]),zeei=str(prediction[0][8]),
                           onze=str(prediction[1][0]),onon=str(prediction[1][1]),ontw=str(prediction[1][2]),onth=str(prediction[1][3]),onfo=str(prediction[1][4]),onfi=str(prediction[1][5]),onsi=str(prediction[1][6]),onse=str(prediction[1][7]),onei=str(prediction[1][8]),
                           twze=str(prediction[2][0]),twon=str(prediction[2][1]),twtw=str(prediction[2][2]),twth=str(prediction[2][3]),twfo=str(prediction[2][4]),twfi=str(prediction[2][5]),twsi=str(prediction[2][6]),twse=str(prediction[2][7]),twei=str(prediction[2][8]),
                           thze=str(prediction[3][0]),thon=str(prediction[3][1]),thtw=str(prediction[3][2]),thth=str(prediction[3][3]),thfo=str(prediction[3][4]),thfi=str(prediction[3][5]),thsi=str(prediction[3][6]),thse=str(prediction[3][7]),thei=str(prediction[3][8]),
                           foze=str(prediction[4][0]),foon=str(prediction[4][1]),fotw=str(prediction[4][2]),foth=str(prediction[4][3]),fofo=str(prediction[4][4]),fofi=str(prediction[4][5]),fosi=str(prediction[4][6]),fose=str(prediction[4][7]),foei=str(prediction[4][8]),
                           fize=str(prediction[5][0]),fion=str(prediction[5][1]),fitw=str(prediction[5][2]),fith=str(prediction[5][3]),fifo=str(prediction[5][4]),fifi=str(prediction[5][5]),fisi=str(prediction[5][6]),fise=str(prediction[5][7]),fiei=str(prediction[5][8]),
                           sizo=str(prediction[6][0]),sion=str(prediction[6][1]),sitw=str(prediction[6][2]),sith=str(prediction[6][3]),sifo=str(prediction[6][4]),sifi=str(prediction[6][5]),sisi=str(prediction[6][6]),sise=str(prediction[6][7]),siei=str(prediction[6][8]),
                           seze=str(prediction[7][0]),seon=str(prediction[7][1]),setw=str(prediction[7][2]),seth=str(prediction[7][3]),sefo=str(prediction[7][4]),sefi=str(prediction[7][5]),sesi=str(prediction[7][6]),sese=str(prediction[7][7]),seei=str(prediction[7][8]),
                           eize=str(prediction[8][0]),eion=str(prediction[8][1]),eitw=str(prediction[8][2]),eith=str(prediction[8][3]),eifo=str(prediction[8][4]),eifi=str(prediction[8][5]),eisi=str(prediction[8][6]),eise=str(prediction[8][7]),eiei=str(prediction[8][8]),
                           )


if __name__ == "__main__":
    app.run(port=5000)



"""
d = ['ze','on','tw','th','fo','fi','si','se','ei']
l=[]
for i,num1 in enumerate(d):
    for j,num2 in enumerate(d):
        t= num1+num2+'='+'str(prediction[{}][{}])'.format(i,j)+','
        l.append(t)


a=[]
for o in d:
    for k in d:
        t=o+k
        a.append(t)

"""











