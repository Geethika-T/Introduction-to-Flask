from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def messages():
    return render_template('message.html')

@app.route('/user/<uname>')
def message(uname):
      return render_template('message.html',name=uname)

@app.route('/table/<int:num>')
def table(num):
      return render_template('print-table.html',n=num)

@app.route('/registration')
def registration():
      return render_template('form.html')

if __name__ == '__main__':
   app.run(debug = True)