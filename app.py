import os, requests, sqlite3, re, datetime, pytz

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

def obtener_fecha_venezuela():
    """Obtiene la fecha actual en la zona horaria de Venezuela en formato YYYY-MM-DD."""
    zona_horaria_venezuela = pytz.timezone('America/Caracas')
    fecha_utc = datetime.datetime.now(datetime.UTC)
    fecha_venezuela = fecha_utc.replace(tzinfo=pytz.utc).astimezone(zona_horaria_venezuela)
    return fecha_venezuela.strftime('%Y-%m-%d')

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
        subject_strategy = request.form.get("strategy")

        if selected_subject:
            session["selected_subject"] = selected_subject

            return redirect("/grades")
        else:
            session["subject_strategy"] = subject_strategy

            return redirect("/strategies")
    else: 
        # Querying subjects that the teacher are teaching
        subjects = db.execute("""
            SELECT s.id, s.name, d.field, s.semester
            FROM subjects s
            JOIN departments d ON s.department_id = d.id
            JOIN teaching t ON s.id = t.subject_id
            JOIN teachers ts ON t.teacher_id = ts.id
            WHERE t.teacher_id = ?
        """, session["user_id"])

        # Querying subject's name
        instructor = db.execute("SELECT names, last_names FROM teachers WHERE id = ?", session["user_id"])

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
                UPDATE grades SET grade = ?, teacher_id = ?, date = ? 
                WHERE student_id = ?
                AND subject_id = ?
            """, int(grade), session["user_id"], obtener_fecha_venezuela(), id_student, id_subject)
        else:
            return apology("wrong data error", 400)

        return redirect("/grades")
    
    else:  
        # List of students
        list_students = db.execute("""
            SELECT students.id, students.names, students.last_names, grades.grade
            FROM studying
            JOIN grades ON studying.student_id = grades.student_id AND studying.subject_id = grades.subject_id
            JOIN students ON studying.student_id = students.id
            WHERE studying.subject_id = ?
        """, session.get("selected_subject"))

        subject_name = db.execute("""
            SELECT name FROM subjects WHERE id = ?
        """, session.get("selected_subject"))

        return render_template("grades.html", list_students=list_students, subject_name=subject_name)
    

@app.route("/strategies", methods=["GET", "POST"])
@login_required
def strategies():
    # List of students who are studying the selected subject
    if request.method == "POST":
        # Getting the info provided by a teacher
        subject_id = request.form.get("subject_id")
        type = request.form.get("type")
        topic = request.form.get("topic")
        percentage = request.form.get("percentage")
        date = request.form.get("date")

        if not subject_id or not type or not topic or not percentage or not date:
            return apology("incomplete data error", 400)

        db.execute("""
            INSERT INTO strategies (type, topic, percentage, subject_id, teacher_id, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, type, topic, percentage, subject_id, session["user_id"], date)

        return redirect("/strategies")
    
    else:  
        # List of students
        list_strategies = db.execute("""
            SELECT id, type, topic, percentage, date
            FROM strategies
            WHERE subject_id = ? AND teacher_id = ?
        """, session.get("subject_strategy"), session["user_id"])

        subject_name = db.execute("""
            SELECT id, name FROM subjects WHERE id = ?
        """, session.get("subject_strategy"))

        return render_template("strategies.html", list_strategies=list_strategies, subject_name=subject_name)


@app.route("/strategies_grades", methods=["GET", "POST"])
@login_required
def strategies_grades():
    # Changing a specific strategy grade
    if request.method == "POST":
        print("strategies_grades")

        return redirect("/strategies_grades")
    
    else:  
        # List of students who must take this strategy
        strategy_id = int(request.args.get("strategy_id"))

        list_students = db.execute("""
            SELECT students.id, students.names, students.last_names, grades.grade
            FROM studying
            JOIN grades ON studying.student_id = grades.student_id AND studying.subject_id = grades.subject_id
            JOIN students ON studying.student_id = students.id
            WHERE studying.subject_id = ?
        """, session.get("subject_strategy"))

        strategy_selected = db.execute("""
            SELECT type, topic, percentage, date
            FROM strategies
            WHERE id = ?
        """, strategy_id)

        return render_template("strategies_grades.html", list_students=list_students, strategy_selected=strategy_selected)

@app.route("/student")
@login_required
def student():
    # Student main page
    subjects = db.execute("""
        SELECT subjects.name, subjects.semester, subjects.credits, grades.grade, teachers.names, teachers.last_names
        FROM studying
        JOIN subjects ON studying.subject_id = subjects.id
        JOIN grades ON studying.student_id = grades.student_id AND studying.subject_id = grades.subject_id
        JOIN teaching ON studying.subject_id = teaching.subject_id
        JOIN teachers ON teaching.teacher_id = teachers.id
        WHERE studying.student_id = ?
    """, session["user_id"])

    learner = db.execute("""
        SELECT names, last_names FROM students WHERE id = ?
    """, session["user_id"])

    return render_template("student.html", subjects=subjects, learner=learner)


@app.route("/add_subjects", methods=["GET", "POST"])
@login_required
def add_subjects():
    if request.method == "POST":

        adding = request.form.get("selected")

        # Checking if there's a teacher teaching that subject
        teaching = db.execute("""
            SELECT teacher_id
            FROM teaching
            WHERE subject_id = ?     
        """, adding)

        # Checking if student already enrolled the subject
        subjects = db.execute("""
            SELECT subject_id
            FROM studying
            WHERE student_id = ?
            AND subject_id = ?
        """, session["user_id"], adding)

        if len(teaching) == 0:
            return apology("there's no teacher yet", 400)
        elif len(subjects) == 1:
            return apology("registered subject", 400)
        else:
            db.execute("""
                INSERT INTO studying (student_id, subject_id) VALUES (?, ?)
            """, session["user_id"], adding)

            db.execute("""
                INSERT INTO grades (student_id, subject_id, grade, teacher_id) VALUES (?, ?, ?, ?)
            """, session["user_id"], adding, 0, teaching[0]["teacher_id"])
            
            flash("Subject added!", "success")
            return redirect("/student")
    
    else:   
            
        subjects_available = db.execute("""
            SELECT subjects.id, subjects.name, subjects.semester, subjects.credits
            FROM subjects
            JOIN students ON subjects.department_id = students.department_id
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
            student = db.execute("SELECT id, pw FROM students WHERE id = ?", id)

            # Ensure username exists and password is correct
            if len(student) != 1 or not check_password_hash(student[0]["pw"], password):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = student[0]["id"]

            return redirect("/student")
        
        elif i_am == "teacher":
            session["role"] = "teacher"
            # Query database for teacher
            teacher = db.execute("SELECT id, pw FROM teachers WHERE id = ?", id)

            # Ensure username exists and password is correct
            if len(teacher) != 1 or not check_password_hash(teacher[0]["pw"], password):
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
            SELECT subject_id
            FROM teaching
            WHERE teacher_id = ?
            AND subject_id = ?
        """, session["user_id"], selected)

        already = db.execute("""
            SELECT subject_id
            FROM teaching
            WHERE subject_id = ?
        """, selected)

        if len(teaching) == 1:
            return apology("registered subject", 400)
        elif len(already) == 1:
            return apology("another teacher already teachs this subject", 400)
        else:
            db.execute("""
                INSERT INTO teaching (teacher_id, subject_id) 
                VALUES(?, ?)
            """, session["user_id"], selected)

            return redirect("/")
        
    else:  

        subjects = db.execute("""
            SELECT subjects.id, subjects.name, departments.field, subjects.semester
            FROM subjects 
            JOIN departments ON subjects.department_id = departments.id
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

        email = request.form.get("email")
        phone = request.form.get("phone")

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
            
            if not email or not phone:
                try:
                    db.execute("""
                        INSERT INTO students (id, names, last_names, pw, department_id) 
                        VALUES(?, ?, ?, ?, ?)
                    """, id, names, surnames, password, faculty)
                except ValueError:
                    return apology("registered username", 400)
            else:
                try:
                    db.execute("""
                        INSERT INTO students (id, names, last_names, pw, department_id, email, phone) 
                        VALUES(?, ?, ?, ?, ?, ?, ?)
                    """, id, names, surnames, password, faculty, email, phone)
                except ValueError:
                    return apology("registered username", 400)
        
        elif i_am == "teacher":
            if not unique_code or unique_code != "TEACHER-00":
                return apology("incorrect teacher code", 400)
            
            if not email or not phone:
                try:
                    db.execute("""
                        INSERT INTO teachers (id, names, last_names, pw)
                        VALUES(?, ?, ?, ?)
                    """, id, names, surnames, password)
                except ValueError:
                    return apology("registered username", 400)
            else:
                try:
                    db.execute("""
                        INSERT INTO teachers (id, names, last_names, pw, email, phone)
                        VALUES(?, ?, ?, ?, ?, ?)
                    """, id, names, surnames, password, email, phone)
                except ValueError:
                    return apology("registered username", 400)
            
        flash('Registered!', 'success')
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
            update = db.execute("SELECT pw FROM students WHERE id = ?", session["user_id"])
            print(update)
            if check_password_hash(update[0]['pw'], old):
                if new == again:
                    new = generate_password_hash(again, method='scrypt', salt_length=16)
                    db.execute("UPDATE students SET pw = ? WHERE id = ?", new, session["user_id"])
                else:
                    return apology("both passwords don't match", 400)
            else:
                return apology("incorrect password", 403)
            
            flash('Password changed!', 'success')
            return redirect('/student')
            
        elif session["role"] == "teacher":
            update = db.execute("SELECT pw FROM teachers WHERE id = ?", session["user_id"])

            if check_password_hash(update[0]['pw'], old):
                if new == again:
                    new = generate_password_hash(again, method='scrypt', salt_length=16)
                    db.execute("UPDATE teachers SET pw = ? WHERE id = ?", new, session["user_id"])
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
