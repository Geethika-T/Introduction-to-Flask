from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def statics():
    return render_template('messages.html')


if __name__ == '__main__':
        app.run(debug=True)