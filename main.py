from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/add", methods=['POST'])
def addinput():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    usernameerror = ''
    passworderror = ''
    emailerror = ''
    validemail = False

    # if the user typed nothing at all, redirect and tell them the error
    if (not username) or (username.strip() == ""):
        usernameerror = "That's not a valid username"
        return redirect("/?error=" + usernameerror)

    if (not password) or (password.strip() == ""):
        passworderror = "That's not a valid password"
        return redirect("/?error=" + passworderror)

    if (not verifypassword) or (verifypassword.strip() == ""):
        passworderror = "That's not a valid password"
        return redirect("/?error=" + passworderror)
    
    if (len(username) < 3) or (len(username) > 20):
        usernameerror = "That's not a valid username"
        return redirect("/?error=" + usernameerror)
    
    if (len(password) < 3) or (len(password) > 20):
       passworderror = "That's not a valid password"
       return redirect("/?error=" + passworderror)

    if (len(email) < 3) or (len(email) > 20):
       emailerror = "That's not a valid email"
       return redirect("/?error=" + emailerror)
    
    if password != verifypassword:
        passworderror = "Passwords don't match"
        return redirect("/?error=" + passworderror)    
    
    for char in username:
        if char == ' ':
            usernameerror = "That's not a valid username"
            return redirect("/?error=" + usernameerror)

    for char in password:
        if char == ' ':
            passworderror = "That's not a valid password"
            return redirect("/?error=" + passworderror)
    
    for char in email:
        if char == ' ':
            emailerror = "That's not a valid email"
            return redirect("/?error=" + emailerror)
        elif char == '@' or char == '.':
            validemail = True
        else:
            if validemail == False:
               emailerror = "That's not a valid email"
               return redirect("/?error=" + emailerror)


     # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    """username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verifypassword_escaped = cgi.escape(verifypassword, quote=True)
    email_escaped = cgi.escape(email, quote=True)
"""
    
    # TODO:
     # Use that template to render the welcome message
     # if no error, then print welcome mesg
     # else print home.html form with error messages 
    #return render_template('welcome.html', username=username_escaped)
    if not usernameerror and not passworderror and not emailerror:
        template = jinja_env.get_template('welcome.html')
        return template.render(username=username)
    else:
        template = jinja_env.get_template('home.html')
        return template.render(usernameerror=usernameerror, passworderror=passworderror, emailerror=emailerror)


@app.route ("/welcome")
def welcomemsg():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

@app.route("/")
def index():
    template = jinja_env.get_template('home.html')
    return template.render()


app.run()