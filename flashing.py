from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "abd"

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    error =None;
    if request.method == "POST":
        if request.form['pass']!='jtp':
            error = "Invalid password"
        else:
            flash("You are successfully logged in")
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

if __name__ == '__main__':
    app.run(debug=True)