from flask import Flask, render_template, request, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect ('/dojos')

@app.route("/dojos")
def all_dojos():
    dojos = Dojo.get_all_dojo()
    print(dojos)
    return render_template("all_dojos.html", all_dojos=dojos)

# @app.route("/create_dojo")
# def create_dojo():
#     return render_template("all_dojos.html")

from flask_app.models.dojo import Dojo
@app.route('/created_dojo', methods=["POST"])
def created_dojo():
    db_data = {
        "name": request.form["name"]
    }
    new_dojo_id=Dojo.save(db_data)
    return redirect ('/dojos')

from flask_app.models.dojo import Dojo
@app.route("/one_dojo/<int:id>")
def one_dojo(id):
    db_data = {
        'id': id
    }
    return render_template("one_dojo.html", dojo = Dojo.get_one_dojo(db_data))

@app.route('/edit_dojo/<int:id>')
def edit_dojo(id):
    db_data = {
        'id': id,
    }
    return render_template("update_dojo.html", dojo = Dojo.get_one_dojo(db_data))

@app.route('/update_dojo', methods=['POST'])
def update_dojo():
    Dojo.update_dojo(request.form)
    new_dojo_id = request.form["id"]
    return redirect(f'/one_dojo/{new_dojo_id}')

@app.route('/delete_dojo/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Dojo.delete_dojo(data)
    return redirect('/dojos')