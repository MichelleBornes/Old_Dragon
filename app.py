# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.character_controller import gerar_classico, gerar_aventureiro, gerar_heroico, montar_personagem
from model.raca import RACAS
from model.classe import CLASSES
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "troque-essa-chave-para-producao")

@app.route("/", methods=["GET"])
def index():
    # página inicial: nome do personagem + escolha de estilo de atributos
    racas = list(RACAS.keys())
    classes = list(CLASSES.keys())
    return render_template("index.html", racas=racas, classes=classes)

@app.route("/generate", methods=["POST"])
def generate():
    nome = request.form.get("nome", "").strip()
    estilo = request.form.get("estilo")
    if not nome:
        flash("Informe o nome do personagem.")
        return redirect(url_for("index"))

    session.clear()
    session["nome"] = nome
    session["estilo"] = estilo

    if estilo == "classico":
        atributos = gerar_classico()
        session["atributos"] = atributos  # JSON-serializável
        # já temos os atributos finais — pular etapa de distribuição
        return redirect(url_for("select_race_class"))
    elif estilo == "aventureiro":
        rolagens = gerar_aventureiro()
        session["rolagens"] = rolagens
        return redirect(url_for("assign"))
    elif estilo == "heroico":
        rolagens = gerar_heroico()
        session["rolagens"] = rolagens
        return redirect(url_for("assign"))
    else:
        flash("Estilo inválido.")
        return redirect(url_for("index"))

@app.route("/assign", methods=["GET", "POST"])
def assign():
    # página para o usuário distribuir rolagens entre os atributos (aventureiro/heroico)
    estilo = session.get("estilo")
    rolagens = session.get("rolagens", [])
    atributos_base = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    if request.method == "POST":
        # receber os valores escolhidos para cada atributo
        chosen = {}
        usados = []
        for atr in atributos_base:
            val = request.form.get(atr)
            if val is None:
                flash("Preencha todos os atributos.")
                return redirect(url_for("assign"))
            try:
                v = int(val)
            except ValueError:
                flash("Valor inválido.")
                return redirect(url_for("assign"))
            chosen[atr] = v
            usados.append(v)
        # validar que a multiconjunto usado bate com rolagens (mesma multiconjunto)
        # comparar contagens
        from collections import Counter
        if Counter(usados) != Counter(rolagens):
            flash("Distribuição inválida: os valores escolhidos não correspondem às rolagens disponíveis.")
            return redirect(url_for("assign"))
        session["atributos"] = chosen
        return redirect(url_for("select_race_class"))

    # GET: mostrar formulário de distribuição
    return render_template("assign.html", estilo=estilo, rolagens=rolagens, atributos_base=atributos_base)

@app.route("/select", methods=["GET", "POST"])
def select_race_class():
    # selecionar raça e classe depois que atributos já existem
    racas = list(RACAS.keys())
    classes = list(CLASSES.keys())
    atributos = session.get("atributos")
    if not atributos:
        flash("Atributos não encontrados. Gere novamente.")
        return redirect(url_for("index"))

    if request.method == "POST":
        raca = request.form.get("raca")
        classe = request.form.get("classe")
        nome = session.get("nome")
        personagem = montar_personagem(nome, atributos, raca, classe)
        session["personagem"] = personagem.as_dict()
        return redirect(url_for("sheet"))

    return render_template("select.html", racas=racas, classes=classes, atributos=atributos)

@app.route("/sheet")
def sheet():
    personagem = session.get("personagem")
    if not personagem:
        flash("Personagem não encontrado.")
        return redirect(url_for("index"))
    return render_template("sheet.html", personagem=personagem)

if __name__ == "__main__":
    app.run(debug=True)
