import requests

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400, template="because", redirect_url="/"):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s
    
    meme = {
        "default": "https://api.memegen.link/images/custom/",
        "because": "https://api.memegen.link/images/because/"
    }[template]

    return render_template("apology.html", top=code, bottom=escape(message), meme=meme, redirect_url=redirect_url), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return redirect("/admin_login")
        return f(*args, **kwargs)
    return decorated_function