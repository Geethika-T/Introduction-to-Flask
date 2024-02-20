from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/ceo")
def ceo():
    return "This is the CEO of the company"

@app.route("/manager")
def manager():
    return "This is the manager of the company"

@app.route("/employee")
def employee():
    return "This is the employee of the company"

@app.route("/user/<name>")
def user(name):
    if name == "ceo":
        return redirect(url_for('ceo'))
    if name == "manager":
        return redirect(url_for('manager'))
    if name == "employee":
        return redirect(url_for('employee'))

if __name__ == "__main__":
    app.run(debug=True)
