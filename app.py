from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import os

app = Flask(__name__)
app.secret_key = "secret_key"

# Database Configuration (Render Safe)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or \
    "sqlite:///" + os.path.join(basedir, "database.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ------------------ USER MODEL ------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )


with app.app_context():
    db.create_all()


# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------- REGISTER (WITH VALIDATION) --------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"].strip()

        # Empty Validation
        if not name or not email or not password:
            flash("All fields are required!", "danger")
            return render_template("register.html")

        # Password Length Validation
        if len(password) < 6:
            flash("Password must be at least 6 characters long!", "danger")
            return render_template("register.html")

        # Unique Email Check
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "danger")
            return render_template("register.html")

        # Create User
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"].strip()

        if not email or not password:
            flash("All fields are required!", "danger")
            return render_template("login.html")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["email"] = user.email
            return redirect("/dashboard")
        else:
            flash("Invalid email or password!", "danger")
            return render_template("login.html")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    if "email" in session:
        user = User.query.filter_by(email=session["email"]).first()
        return render_template("dashboard.html", user=user)
    return redirect("/login")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.pop("email", None)
    flash("Logged out successfully!", "success")
    return redirect("/login")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)