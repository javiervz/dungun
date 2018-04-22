#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from mapu_verbs import verb_to_mapudungun

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/', methods=["POST"])

verbos=pd.read_csv('verbs.csv',header=0,sep='\t')
verbos_esp=[verbo for verbo in verbos.esp]
verbos_mapu=[verbo for verbo in verbos.mapu]
verbos={esp:mapu for (esp,mapu) in zip(verbos_esp,verbos_mapu)}

def transformed():
  text = request.form['text']
  output=verb_to_mapudungun(text,verbos)
  return output#render_template("results.html", output=output)

if __name__ == '__main__':
    app.run()
  

