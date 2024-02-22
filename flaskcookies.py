from flask import Flask, make_response

app = Flask(__name__)

@app.route('/cookie')
def cookie():
    res=make_response("<h1>Cookie is set</h1>")
    res.set_cookie('abc','cdf')
    return res

if __name__ =='__main__':
    app.run(debug=True)