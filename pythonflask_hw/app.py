from flask import Flask, Response, url_for, render_template

app = Flask(__name__)

# the decorator(a wrapper function) uses flask to bind the url to the function


@app.route('/')
def hello_from_flask():
    return render_template('index.html')


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
    return """
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact us</h1>
<nav>
    <div align="right;">
        <form>
            <button formaction="http://127.0.0.1:5000/">Home</a></button>
        </form>
        <form>    
            <button formaction="http://127.0.0.1:5000/about_us" target="_blank">About Us</a></button>
        </form>
    </div>
</nav>   
<section>
<div>

    <p>Contacting us has never been easier.</p>
    <br>        
    <hr style="border: 1px solid lightgrey">
    <p>Call (020) 0800 1233.</p>
    <p>Phone lines are open 08:00-16:00 GMT.</p>
    <hr style="border: 1px solid lightgrey">
    <p>Email: girls@work.com</p>
    <p>All emails will be responded to within 48 hours.</p>
    <hr style="border: 1px solid lightgrey">
    <p>Visit our office </p>
    <p>Please adhere to the relevant government Covid-19 guidelines.</p>
    <p>87-135 Brompton Road, Knightsbridge</p>
    <p>London SW1x 7XL</p>
    <hr style="border: 1px solid lightgrey">
</body>
</html>
"""


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
  border-radius: 15px;
 background: #ae70d2;
  padding: 20px;
  width: 98%;
  height: 150px;
  float: centre;
  text-align: center;
  font-size: 35px;
  color: white;
}
body {background-color:#d2ae70;}
h1  {text-align: center;
    margin: 30px;
}
h3  {text-align: center;
    border-radius: 15px;
    width: 80%;
    margin: 50px;
    background-color:#70d2ae;
}
nav{height 
padding: 30px;
}
p{background: #ae70d2;
    border-radius: 15px;
    height: 140px;
    margin: 50px;
    float: left;
    padding: 3%;
    width: 70%;
    background-color: #70d2ae;
    text-align: center;
}
.myDiv{width: 30%;
    background-color: #FFFF66;
    padding: 15;
    border-radius: 15px;
    height: 150px;
    margin: 20px;
}
aside{width: 25%;
    background-color: #FFFF99;
    border-radius: 15px;
    padding: 15;
    height: 150px;
    margin: 50px;
}
footer{color: white;
    padding: 15px;
    border-radius: 15px;
    height: 20px;
    margin: 10px;
    background-color: #ae70d2;
    text-align: centre;
}
@media (max-width: 600px) {
  nav, article {
    width: 100%;
    height: auto;
}
</style>
</head>
<body>
<header>
    <div>
        <h1>All about us</h1>
    </div>
    <div align="left">
        <h3>Read on to find out more about us.</h3>
    </div>
</header>
<nav>
    <div align="right">
        <form>
            <button formaction="http://127.0.0.1:5000/">Home</a></button>
        </form>
        <form>    
            <button formaction="http://127.0.0.1:5000/contact_us" target="_blank">Contact Us</a></button>
        </form>
    </div>
</nav>
<section>
    <img src="/static/group_of_minions.jpg" style="float:right; margin-right:10px; 
    width=400px; border:none; border-radius: 25px;" alt="A group of fun loving minions">
    <div class=myDiv>
    We're part of Sky's Get into Tech, London Cohort - January 2021.
    <br>
    Our group consists of five software developers...in training. 
    
    
            <ol>
                <li>Asia</li>
                <li>Faridah</li>
                <li>Michelle</li>
                <li>Sanele</li>
                <li>Tasnim</li>
            </ol>
    </div>
</section>
<aside align="left">
    <div>
        Our interests include:
            <ul>
                <li>Collaboration</li>
                <li>Version control</li>
                <li>YouTube videos</li>
                <li>Python programming</li>
                <li>JavaScript and React</li>
                <li>Machine learning</li>
            </ul>  
    </div>
</aside>
<footer>For further information: girls@work.com
    &nbsp; &copy; Sky Get into Tech, 2021 
    <a href="https://www.pinterest.com/pin/create/button/" data-pin-do="buttonBookmark">
</a>
</footer>
</body>
<script
    type="text/javascript"
    async defer
    src="//assets.pinterest.com/js/pinit.js">
</script>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)
