from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)
lista = []

@app.route("/")
def inicio():
    return render_template("inicio.html", nomes=lista)

@app.route("/novo")
def novo():
    return render_template("novo.html")

@app.route("/criar", methods=["POST",])
def criar():
    nome = request.form["nome"]
    lista.append(nome)
    return redirect("/")

@app.route("/editar/<id>")
def editar(id):
    id = int(id)
    return render_template("editar.html", nome=lista[id],id=id)

@app.route("/atualizar", methods=["POST",])
def atualizar():
    nome = request.form["nome"]
    id = int(request.form["id"])
    lista[id] = nome
    return redirect ("/")

@app.route("/deletar/<id>")
def deletar(id):
    id = int(id)
    del lista[id]
    return redirect("/")

app.run(debug=True)