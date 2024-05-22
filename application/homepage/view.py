from flask import Blueprint, redirect , url_for, render_template, request, flash
from .models import Person
from ..extensions import db


bp = Blueprint("home",__name__,url_prefix="/",template_folder="pages")

@bp.route("/")
def home():
    persons = Person.query.all()
    return render_template("homepage/home.html", persons=persons)

@bp.route("/add", methods={"GET","POST"})
def add():
    # validation
    def validated(last_name, first_name):
        valid = True 

        if not last_name:
            flash("Please type Last Name")
            valid = False
        if not first_name:
            flash("Please type First Name")
            valid = False
        return valid

    if request.method == "POST":
        #  Save
        last_name = request.form["last_name"]
        first_name = request.form.get("first_name")

        if validated(last_name, first_name):
            person = Person(  
                last_name=last_name,
                first_name=first_name
            )
            db.session.add(person)
            db.session.commit()
            return  redirect("/")

    return render_template("homepage/add.html")

@bp.route("/delete/<person_id>")
def delete(person_id):
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()

    return redirect("/")

@bp.route("/edit/<person_id>", methods={"GET","POST"})
def edit(person_id):
    person = Person.query.get(person_id)
    
    def validated(last_name, first_name):
        valid = True 

        if not last_name:
            flash("Please type Last Name")
            valid = False
        if not first_name:
            flash("Please type First Name")
            valid = False
        return valid

    if request.method == "POST":
        #  Save
        last_name = request.form["last_name"]
        first_name = request.form.get("first_name")

        if validated(last_name, first_name):
           person.last_name = last_name
           person.first_name = first_name
           db.session.commit()

           return  redirect("/")
        
    return render_template("homepage/edit.html", person=person)


@bp.route("/create")
def create():
    db.create_all()
    return redirect(url_for("home.home"))
