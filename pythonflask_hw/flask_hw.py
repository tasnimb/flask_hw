from flask import Flask, Response, url_for, render_template

app = Flask(__name__)

# the decorator(a wrapper function) uses flask to bind the url to the function


@app.route('/')
def hello_from_flask():
    return render_template('webpage.html')


@app.route('/dynamic/<word>')
def home(word):
    return word


@app.route('/greet/<name>')
def greet(name):
    return """
<html>
<head>
    <title>Simple-Flask routes</title>
<head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
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
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {} !</p>
    <p>You are {} year(s) old.</p>
    <hr>
    <a href='{}'> Welcome</a>
</body>
</html>
""".format(name, age, url)


@app.route('/contact_us')
def contact():
    return "email us at gmail.com"


@app.route('/about_us')
def about_us():
    return """
<html>
<head>
    <title>All about us</title>
<style>
    {box-sizing: border-box;
}
html{font-family: "Roboto", "Arial","sans-serif";
    color: black;
}
header{background-color: #ae70d2;
  padding: 50px;
  text-align: center;
  font-size: 35px;
  color: white;
}
body {background-color:#d2ae70;}
h1  {border: 15px solid darkgrey;
    background-color: darkgrey;
    text-align: center;
    margin: 50px;
}
paragraph{border: 0;
    margin: 50px;
    float: left;
    padding: 20px;
    width: 70%;
    background-color: #70d2ae;
    text-align: center;
}
.myDiv{width: 25%;
    background_color: #70d2ae;
    float: left;}
aside{width: 25%;
    background_color: #70d2ae;
    float: left;}
footer{color: royalblue;
    border: 0;
    background-color: #70d2ae;
    text-align: left;
    margin: 20px;
}
@media (max-width: 600px) {
  nav, article {
    width: 100%;
    height: auto;
}
</style>
<head>
<body>
<header>
    <div>
        <h1>All about us</h1>
        <p>Read on to find out more about us.</p>
    </div>
</header>
<navigation>
    <div>
        <button class="button button2" <a href="http://127.0.0.1:5000/">Home</a></button>
        <button class="button button2" <a href="http://127.0.0.1:5000/contact_us" target="_blank">Contact Us</a></button>
    </div>
</navigation>
<aside>
    <div>
        <p>Our interests include:
            <ul>
                <li>Version control</li>
                <li>YouTube videos</li>
                <li>Python programming</li>
                <li>Colloboration</li>
            </ul>
        </p>
    </div>
</aside>
<section>
    <div class=myDiv>
        <p> Our group consists of five software developers...in training.</p>
            <ol>
                <li>Asia</li>
                <li>Faridah</li>
                <li>Michelle</li>
                <li>Sanele</li>
                <li>Tasnim</li>
            </ol>
        </p>
    </div>
    <img src="/images/group_of_minions.jpg" alt="A group of fun loving minions" width="200px;">
</section>
<footer><p>&copy; Sky Get into Tech, 2021 
    For further information: girls@work.com</p>
</footer>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)
