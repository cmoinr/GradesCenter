import os
import requests
import sqlite3
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///gradescenter.db")


@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    # Teacher main page
    if request.method == "POST":
        # Redirect to selected subject's list of students
        selected_subject = request.form.get("check")

        session["selected_subject"] = selected_subject

        return redirect("/grades")
    else: 
        # Querying subjects that the teacher are teaching
        subjects = db.execute("""
            SELECT subjects.id, subjects.name, faculty.field, subjects.semester, subjects.year
            FROM subjects
            JOIN faculty ON subjects.id_faculty = faculty.id
            JOIN teaching ON subjects.id = teaching.id_subject
            JOIN teachers ON teaching.id_teacher = teachers.id
            WHERE teaching.id_teacher = ?
        """, session["user_id"])

        # Querying subject's name
        instructor = db.execute("SELECT names, surnames FROM teachers WHERE id = ?", session["user_id"])

        return render_template("index.html", subjects=subjects, instructor=instructor)


@app.route("/grades", methods=["GET", "POST"])
@login_required
def grades():
    # List of students who are studying the selected subject
    if request.method == "POST":
        # Getting the grade provided by a teacher
        grade = request.form.get("grade")
        id_student = request.form.get("id_student")
        id_subject = session.get("selected_subject")

        if not id_student or not grade:
            return apology("incomplete data error", 400)
        
        if int(grade) >= 0 or int(grade) <= 10:
            db.execute("""
                UPDATE grades SET grade = ? 
                WHERE id_student = ?
                AND id_subject = ?
            """, int(grade), id_student, id_subject)
        else:
            return apology("wrong data error", 400)

        return redirect("/grades")
    
    else:  
        # List of students
        list_students = db.execute("""
            SELECT students.id, students.names, students.surnames, grades.grade
            FROM students
            JOIN studying ON students.id = studying.id_student
            JOIN grades ON studying.id_subject = grades.id_subject
            WHERE studying.id_subject = ?
        """, session.get("selected_subject"))

        subject_name = db.execute("""
            SELECT name FROM subjects WHERE id = ?
        """, session.get("selected_subject"))

        return render_template("grades.html", list_students=list_students, subject_name=subject_name)


@app.route("/student")
@login_required
def student():
    # Student main page
    subjects = db.execute("""
        SELECT subjects.name, subjects.semester, subjects.year, subjects.credits, grades.grade, teachers.names, teachers.surnames
        FROM studying
        JOIN students ON studying.id_student = students.id
        JOIN grades   ON studying.id_subject = grades.id_subject
        JOIN subjects ON studying.id_subject = subjects.id
        JOIN teaching ON studying.id_subject = teaching.id_subject
        JOIN teachers ON teaching.id_teacher = teachers.id
        WHERE studying.id_student = ?
    """, session["user_id"])

    learner = db.execute("""
        SELECT names, surnames FROM students WHERE id = ?
    """, session["user_id"])

    return render_template("student.html", subjects=subjects, learner=learner)


@app.route("/add_subjects", methods=["GET", "POST"])
@login_required
def add_subjects():
    if request.method == "POST":

        adding = request.form.get("selected")

        subjects = db.execute("""
            SELECT id_subject
            FROM studying
            WHERE id_student = ?
            AND id_subject = ?
        """, session["user_id"], adding)

        if len(subjects) == 1:
            return apology("registered subject", 400)
        else:
            db.execute("""
                INSERT INTO studying (id_student, id_subject) VALUES (?, ?)
            """, session["user_id"], adding)

            db.execute("""
                INSERT INTO grades (id_student, id_subject, grade) VALUES (?, ?, ?)
            """, session["user_id"], adding, 0)
            
            return redirect("/student")
    
    else:   
            
        subjects_available = db.execute("""
            SELECT subjects.id, subjects.name, subjects.semester, subjects.year, subjects.credits
            FROM subjects
            JOIN students ON subjects.id_faculty = students.id_faculty
            WHERE students.id = ?
        """, session["user_id"])

        return render_template("add_subjects.html", subjects_available=subjects_available)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Log user in

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        i_am = request.form.get("i_am")
        id = request.form.get("id")
        password = request.form.get("password")

        if not i_am or not id or not password:
            return apology("all fields need to be filled", 400)
        
        if i_am == "student":
            session["role"] = "student"

            # Query database for student
            student = db.execute("SELECT * FROM students WHERE id = ?", id)

            # Ensure username exists and password is correct
            if len(student) != 1 or not check_password_hash(student[0]["hash"], password):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = student[0]["id"]

            return redirect("/student")
        
        elif i_am == "teacher":
            session["role"] = "teacher"
            # Query database for teacher
            teacher = db.execute("SELECT * FROM teachers WHERE id = ?", id)

            # Ensure username exists and password is correct
            if len(teacher) != 1 or not check_password_hash(teacher[0]["hash"], password):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = teacher[0]["id"]

            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/subjects", methods=["GET", "POST"])
@login_required
def subjects():
    if request.method == "POST":

        selected = request.form.get("selected")

        teaching = db.execute("""
            SELECT id_subject
            FROM teaching
            WHERE id_teacher = ?
            AND id_subject = ?
        """, session["user_id"], selected)

        already = db.execute("""
            SELECT id_subject
            FROM teaching
            WHERE id_subject = ?
        """, selected)

        if len(teaching) == 1:
            return apology("registered subject", 400)
        elif len(already) == 1:
            return apology("another teacher already teachs this subject", 400)
        else:
            db.execute("""
                INSERT INTO teaching (id_teacher, id_subject) 
                VALUES(?, ?)
            """, session["user_id"], selected)

            return redirect("/")
        
    else:  

        subjects = db.execute("""
            SELECT subjects.id, name, field, semester, year
            FROM subjects 
            JOIN faculty ON subjects.id_faculty = faculty.id
        """)

        return render_template("subjects.html", subjects=subjects)


@app.route("/register", methods=["GET", "POST"])
def register():
    # Register user
    if request.method == "POST":

        i_am = request.form.get("i_am") 
        id = request.form.get("id")
        names = request.form.get("names")
        surnames = request.form.get("surnames")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        unique_code = request.form.get("unique_code")
        faculty = request.form.get("faculty")

        # Validations
        if not i_am or not id or not names or not surnames or not password or not confirmation:
            return apology("all fields need to be filled", 400)
        
        if not re.match(r"^\d{8}$", id):
            return apology("ID must be only numbers", 400)
        elif not re.match(r"^[a-zA-Z]+$", names) or not re.match(r"^[a-zA-Z]+$", surnames):
            return apology("Invalid names/surnames", 400)
        
        if password == confirmation:
            password = generate_password_hash(confirmation, method='scrypt', salt_length=16)            
        else:
            return apology("both passwords don't match", 400)
        
        if i_am == "student":
            if not faculty:
                return apology("all fields need to be filled", 400)
            
            try:
                db.execute("""
                    INSERT INTO students (id, names, surnames, hash, id_faculty) 
                    VALUES(?, ?, ?, ?, ?)
                """, id, names, surnames, password, faculty)
            except ValueError:
                return apology("registered username", 400)
        
        elif i_am == "teacher":
            if not unique_code or unique_code != "TEACHER-00":
                return apology("incorrect teacher code", 400)
            
            try:
                db.execute("""
                    INSERT INTO teachers (id, names, surnames, hash)
                    VALUES(?, ?, ?, ?)
                """, id, names, surnames, password)
            except ValueError:
                return apology("registered username", 400)

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/edit_pass", methods=["GET", "POST"])
@login_required
def edit_pass():
    if request.method == "POST":
        old = request.form.get("old_password")
        new = request.form.get("new_password")
        again = request.form.get("new_pass_again")

        if not old or not new or not again:
            return apology("all fields need to be filled", 400)


        if session["role"] == "student":
            update = db.execute("SELECT hash FROM students WHERE id = ?", session["user_id"])
            print(update)
            if check_password_hash(update[0]['hash'], old):
                if new == again:
                    new = generate_password_hash(again, method='scrypt', salt_length=16)
                    db.execute("UPDATE students SET hash = ? WHERE id = ?", new, session["user_id"])
                else:
                    return apology("both passwords don't match", 400)
            else:
                return apology("incorrect password", 403)
            
        elif session["role"] == "teacher":
            update = db.execute("SELECT hash FROM teachers WHERE id = ?", session["user_id"])

            if check_password_hash(update[0]['hash'], old):
                if new == again:
                    new = generate_password_hash(again, method='scypt', salt_length=16)
                    db.execute("UPDATE teachers SET hash = ? WHERE id = ?", new, session["user_id"])
                else:
                    return apology("both passwords don't match", 400)
            else:
                return apology("incorrect password", 403)
            

        flash('Password changed!', 'success')
        return redirect('/')

    else:
        return render_template("edit_pass.html")


@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html")
