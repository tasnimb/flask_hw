from flask import Flask, Response, request, url_for, render_template

app = Flask(__name__)

# the decorator(a wrapper function) uses flask to bind the url to the function


@app.route('/')
def hello_from_flask():
    return render_template('webpage.html')


@app.route('/dynamic/<word>')
def home(word):
    return word

# @app.route('/dynamic/greeting/<name>')
# def greet_name(name):
#     new_name = "Hello " + name
#     return new_name


@app.route('/greet/<name>')
def greet(name):
    return """
<html>
<head>
    <title>Simple-Flask routes</title>
<head>

<body>
    <h1> Name page</h1>
    <p> Hello {} !</p>

</body>
</html>
""".format(name)


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route('/greet/<name>/<int:age>')
def greet_age(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
    <title>Simple-Flask routes</title>
<head>

<body>
    <h1> Name page</h1>
    <p> Hello {} !</p>
    <p> You are {} year(s) old.</p>
    <hr>
    <a href='{}'> Welcome </a>

</body>
</html>
""".format(name, age, url)


@app.route('/contact_us')
def contact():
    return "email us at gmail.com"


if __name__ == "__main__":
    app.run(debug=True)
