from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Helloo,Welcome to our website.";

@app.route('/nest/<name>')
def nest(name):
    return "Helloo, " +name;

@app.route('/tree/<int:age>')
def tree(age):
    return "Age = %d" %age;

def about():
    return "This is about page";

app.add_url_rule("/about","about",about)

if __name__ == "__main__":
    app.run(debug = True)
