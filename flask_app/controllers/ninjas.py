from flask import Flask, render_template, request, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# @app.route("/")
# def index():
#     users = User.get_all()
#     print(users)
#     return render_template("read_all.html", all_users=users)

@app.route("/create_ninja")
def create_ninja():
    all_dojos = Dojo.get_all_dojo()
    return render_template("create_ninja.html", all_dojos=all_dojos)

from flask_app.models.ninja import Ninja
@app.route('/created_ninja', methods=["POST"])
def created_ninja():
    db_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    print(db_data)
    new_dojo_id=Ninja.save(db_data)
    return redirect('/dojos')


from flask_app.models.ninja import Ninja
@app.route("/one_ninja/<int:id>")
def read_one(id):
    data = {
        'id': id
    }
    return render_template("one_ninja.html", ninja = Ninja.get_one_ninjas(data))

@app.route('/edit_ninja/<int:ninja_id>')
def edit_ninja(ninja_id):
    all_dojos = Dojo.get_all_dojo()
    data = {
        'id': ninja_id
    }
    Ninja.save(data)
    return render_template("update_ninja.html", ninja = Ninja.get_one_ninjas(data), all_dojos=all_dojos)

@app.route('/update_ninja/<int:ninja_id>', methods=['POST'])
def update_ninja(ninja_id):
    data = {
        'id': ninja_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.update_ninja(data)
    new_dojo_id = request.form["dojo_id"]
    return redirect(f'/one_dojo/{new_dojo_id}')

@app.route('/delete_ninja/<int:id>')
def delete_ninja(id):
    data = {
        'id': id
    }
    ninja = Ninja.get_one_ninjas(data)
    Ninja.delete_ninja(data)
    return redirect(f'/one_dojo/{ninja.dojo_id}')