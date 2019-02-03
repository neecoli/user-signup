from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/", methods=['POST'])
def index():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    # if the user typed nothing at all, redirect and tell them the error
    if (not username) or (username.strip() == ""):
        error = "That's not a valid username."
        return redirect("/?error=" + error)

    if (not password) or (password.strip() == ""):
        error = "That's not a valid password."
        return redirect("/?error=" + error)

    if (not verifypassword) or (verifypassword.strip() == ""):
        error = "That's not a valid password."
        return redirect("/?error=" + error)
    
    

     # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verifypassword_escaped = cgi.escape(verifypassword, quote=True)
    email_escaped = cgi.escape(email, quote=True)
    

    
    # TODO:
     # Use that template to render the welcome message 
    return render_template('home.html', 'welcome.html', username_escaped=username)


app.run()