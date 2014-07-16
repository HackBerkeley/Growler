# Introduction

Welcome! If you've never hacked before, don't worry. This is a guide that will help you through your first hack. We'll be building **Cheeper**, a lightweight, simpler version of Twitter.

TODO end result link

# How to get help

If you find yourself getting stuck, don't just stare at the code for an hour. Instead, do the following:

* **Use Google.** Results from [stackoverflow.com](http://stackoverflow.com) are an amazing resource. You get to utilize the knowledge of the global computer science developer community. However, don't just copy-paste answers from the web. Make sure you understand exactly what's going on before you copy-paste anything.
* **Ask your neighbors.** Working in groups is extremely productive as each of you can fill the gaps of knowledge the others have. Also, it's a good opportunity to make friends and find future potential project partners!
* **Ask H@B members for help.** Several H@B members have volunteered to assist people with this hack.

# Step 1: Make sure you have Python 3.4

**You probably already have Python 3.4 installed** if you're taking CS 61A. To check, type

    python3 --version

in your command line.

- If you have Python 3.4 or greater, go to the next step.
- If you do not have Python 3.4 or greater, you will need to install it. To install Python:

### Windows
Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and click the big yellow download button for Python 3. Then install it.

### Mac
First, make sure you have Homebrew. If not, visit the [Homebrew website](http://brew.sh/) and follow the instructions to install it.

Once you have Homebrew installed, just do `brew install python3` in your Terminal.

### Linux
Type `sudo apt-get install python3` in your Terminal.

# Step 2: Install Flask

Flask is a web app server for Python. It makes it really easy to write web apps. Let's get it installed.

In your command line, type

    pip3 install flask

- If you get the error `'pip3' is not recognized as an internal or external command` blah blah blah, you're probably using Windows. You will need to set your PATH variable so that Windows can locate pip3. You will need to add `C:\<Your Python installation directory here>\Scripts\` to your PATH variable. Ask Google or your neighbor if you're unsure of how to do this, or ask a H@B officer if you're really stuck.

# Step 3: Get coding

Now that you have Flask installed, you can get started. First, create a folder to hold your new project:

    mkdir cheeper
    cd cheeper
    touch server.py

You just created the `cheeper` folder and a `server.py` file inside of it. Now open up `server.py` in your favorite text editor.

// TODO everything below


# Step 2.5: Create your project folder!

This is exciting. Run these commands (you should know what they do):

```
$ mkdir cheeper
$ cd cheeper
```

We want to make the `cheeper` directory a `virtualenv` environment, so we run the command:
```
$ virtualenv venv --distribute
```

If you look inside `cheeper/` now, you'll see that there is a folder called `venv/` with 3 folders inside called `bin/`,`include/`, and `lib/`.

To jump into the `virtualenv` you've created, make sure you're in the `cheeper` directory and run:
```
$ source venv/bin/activate
```

Your terminal prompt should now have a `(venv)` at the front. This is how you know you're inside your virtual environment. 


Whoa, this is awesome. You're in your own sandbox now. You can see what libraries you currently have installed by running:

```
$ pip freeze
```

To leave your `virtualenv`, just run:
```
$ deactivate
```

We'll be in our `virtualenv` in the following sections. If you're curious as to what else it can do, look up more on [this site](https://pypi.python.org/pypi/virtualenv).

Step 3: Setting up Flask
=====================================
[Flask](http://flask.pocoo.org/) is a Python web framework.

After this point, make sure you're working in your `virtualenv`. (It should say "`(venv)`" at the left of your terminal prompt).

To install Flask just run:
```
$ pip install flask
```

Wow that was simple (hopefully)! Remember that if at any point, stuff isn't installing/working properly, ask a neighbour or the nearest H@B office for help.

Okay, so let's get started with Flask. 

First, what exactly is a web framework? When a person goes to a website, they send an HTTP request to that website, asking for the site's content. Since we're building the website, our web framework, Flask, will handle requests that are sent to us, and send back our site's content via HTTP response.

Let's try running the "Hello World" example on the [Flask website](http://flask.pocoo.org).

Copy and paste the example and put it into a file called `server.py`. This code imports Flask, creates an application (`app`), and defines a "route" (we'll go over that in a second), and finally starts up the server.

Try running it to make sure Flask was installed correctly.
```
$ python server.py
```
If it says Flask isn't importing, make sure you're in the `virtualenv`.
If it says something like: "Running on http://127.0.0.1:5000", then it's working! Test it yourself by going to either `localhost:5000` or `127.0.0.1:5000` in your favorite browser. It should say "Hello World!".

> *Note*: both `localhost` and `127.0.0.1` are addresses for your own computer and `5000` is the "port" number.

Now that you have this working, please go through the examples on the Flask [quick start page](http://flask.pocoo.org/docs/quickstart/) and familiarize yourself with the Flask framework. You can stop once you hit [Accessing Request Data](http://flask.pocoo.org/docs/quickstart/#accessing-request-data). Make sure you understand what a route is and how to do routing with Flask. Hint: decorators.

Step 4: Creating a user interface
===========================
Let's create our home page for Cheeper©. Create a directory in your `cheeper` directory called `static`. This will be the folder for our *static* files, or the files that don't change and are just retrieved and sent down by Flask when a browser asks for them.

Your project directory should look like this now:
```
cheeper/
    venv/
        bin/
        include/
        lib/
    server.py
    static/
```

Now inside your static folder, create a file called `index.html`.
In it, put the following skeleton.
```html
<html>
  <head>
    <title>Cheeper - better than Twitter</title>
  </head>
  <body>
  Hello World!
  </body>
</html>
```

This is HTML, or HyperText Markup Language. It's a language that browsers understand and use to render web pages. In HTML files, you define the content and layout of your web page. `index.html` is the canonical name for the default web page that's rendered when you go to a site, so `index.html` will function as the home page.

Right now, if you open the file in your web browser, you'll get a page that says "Hello World!", but on your tab, it should say what we put into the `<title>` tag.

Now, I suggest reading up on the basics of HTML. Make sure you understand how to create forms. Here's a [Codecademy tutorial](http://www.codecademy.com/courses/web-beginner-en-Vfmnp/0/2) on creating web forms for your edification!

So now for some user interface design (which is something I, the writer of this guide, am terrible at, so feel free to rage at my designs). And of course, if you are design inclined yourself, feel free to throw away my suggestions and use your own.

Our Cheeper© webpage should include some glamorous logo and a space to type your cheep and cheep it to the world. We also need a feed, to display all the cheeps that have been cheeped.

First let's add the logo, which will just be really big text. We can do this with the `<h1>`. Add an `<h1>` tag into the body of `index.html`, which will be our logo.

```html
...
<body>
  <h1>Cheeper</h1>
</body>
...
```

Now let's add the form to write and submit your cheeps. Cheeps are only 76 characters long, right?

```html
...
<body>
  <h1>Cheeper</h1>
  <form>
    Name:
    <input name="name" type="text" /> 
    Cheep:
    <input name="cheep" type="text" maxlength="76" /> 
    <input type="submit" />
  </form>
</body>
...
```

Awesome! Our awesome, beautiful user interface is almost done. Let's now add a space for the Cheeper© feed to appear.

```html
...
<body>
  <h1>Cheeper</h1>
  <form>
    Name:
    <input name="name" type="text" /> 
    Cheep:
    <input name="cheep" type="text" maxlength="76" /> 
    <input type="submit" />
  </form>
  <div id="feed">
  </div>
</body>
...
```
Cool! This is possibly the best UI I've ever designed. If you feel that it needs improvement, make it look as pretty as you want. Look into using *CSS*.

Step 5: Serving static webpages
===========================
Our html page, `index.html` is only visible on our own computers right now. We need to hook it up to our Flask server, which is accessible from other computers. We can do this pretty easily with some Flask magic.

Flask's job will be to grab `index.html` and return it for the route `/`, the homepage.

We can do this by modifying our `server.py`. Modify the `hello` method to return `index.html` instead using the `app.send_static_file` method.

```python
...
@app.route("/")
def hello():
    return app.send_static_file('index.html')
...
```

Restart your server to see the changes by going to `localhost:5000`.

> *Note*: You can see your changes to `index.html` immediately by just refreshing, but you need to restart your server (using Ctrl-C) everytime you modify `server.py` to see the changes.


Woot! Your site should now have a basic form for submitting cheeps showing.

Step 6: Sending requests to Flask
==============================
Let's quickly establish the notion of a *front end* and a *back end*. The front end is what the "client," or web browser sees. Anyone who visits your website is considered a user. The back end refers to the the application that handles storing, manipulating, and sending data back to the front end. Specifically in our hack, the front end corresponds to the files in `static/`, as they are what the user sees and interacts with. The back end corresponds with our `server.py`, so far. We'll be adding more files to our back end component later.

Right now, Flask just spits out our `index.html` file. What we now want to do is to send the data inputted into your web form to Flask. In `index.html`, add an `action` attribute and a `method` attribute with the following values to your form.

```html
...
<form action='/api/cheep' method="POST">
  Name:
  <input name="name" type="text" /> 
  Cheep:
  <input name="cheep" type="text" maxlength="76" /> 
  <input type="submit" />
</form>
```

A form's *action* is the URL to which it submits its data. When you click the submit button, the form gathers all its data and sends it as an HTTP request to the given URL. Right now, we're sending the form data to the `/api/cheep` URL. The form's *method* is the HTTP [method](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). Essentially, a POST request means that we want to *store* data on the server.

Now that we send the data, we need to handle the data we receive in Flask.  Let's go back to `server.py`.

First, add `request` to our list of imports from `flask`.
```python
from flask import Flask, request
...
```

The request object allows us to get data and information about incoming HTTP requests.

Now we need to create a route for `/api/cheep` to actually receive the data.

Add the following method into your `server.py` before the `if __name__ == "__main__":`. I'll explain what it does in a bit.

```python
@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    return "Success!"
```

> Note: at this point, you might be wondering what the `@app.route(...)` above the function definition does. It's what we call a function *decorator*. Decorators augments the behavior of a function. The `app.route` decorator makes your ordinary Python function into a server route. Pretty amazing! If you want to read more about decorators, check out [this link](http://www.shutupandship.com/2012/01/python-decorators-i-functions-that.html).

In this new code we just added, we're adding a new route for `/api/cheep`, which would correspond the url `localhost:5000/api/cheep`. We make sure it handles POST requests by modifying the decorator. In the function body itself, we're just printing out the data sent up by the form (for debugging purposes) and then returning a success message.

To test this out, restart your server and go to `localhost:5000`. Fill out your form with some data and hit the submit button. It should take you to a page that says "Success!" on it. Now look back at your server log (your terminal where you started the server). It should say something like: 
```
ImmutableMultiDict([('cheep', u'hello world!'), ('name', u'jbiebz5000')])
```

Don't worry exactly what this means. Just make sure it is filled with the data you submitted.

Step 7: Take a break!
===========================
All right. There's a lot of information coming up. This is a good time to grab a drink, get some food and socialize a bit. Meet all the awesome people around you!

Step 8: Storing our cheeps
===========================
So at this point, our HTML page should be sending successful requests to the Flask server, but our cheeps aren't showing up on our home page!

Our job will now be to store the cheeps that are sent up to Flask. We'll do this with a *database*. A database allows us to store data on the hard disk in some organized fashion; we'll should also be able to retrieve the data from the database easily.

This is a very general pattern for web applications. The user will input some data on the front end. The data will be sent up via an HTTP request to the web server. The web server will then store the data in some sort of database. 

Later, when the user wants to see their data, they'll request data from the web server via HTTP request, the server will ask the database for the data, then send it back down in the HTTP response.

We'll be using the [sqlite](http://www.sqlite.org/about.html) database to store our cheeps. It's conveniently packaged with Python, so we don't need to install anything!

Okay, so what's `sqlite`. Well, you might have heard of SQL before. It stands for *Structured Query Language* and it's a language you use to query a database for data. In SQL databases, data is organized into *tables*, which have rows and columns. `sqlite` is just an example of a SQL database. If you're curious as to what differentiates `sqlite` from other databases, check out the [wiki page](http://en.wikipedia.org/wiki/SQLite).

Let's begin using `sqlite`! If you're curious, you can find the Python documentation for sqlite3 [here](http://docs.python.org/2/library/sqlite3.html).

A database is a collection of tables. You can think of a table sort of like an Excel spreadsheet, where each column is a different piece of information that an entry needs, and each row is an entry in the table.

Let's play with sqlite a bit first. Make a file called `init_db.py` at the top level of your `cheeper` folder. Put the following in.
```python
import sqlite3
conn = sqlite3.connect('cheeps.db')
```
This imports the sqlite package and opens a connection to the database file named `cheeps.db`. If the file doesn't exist, sqlite will create it automatically.
```python
c = conn.cursor()
```
We'll go more into detail on this later. A cursor basically points to a specific row in the database, which allows a programmer to make changes row by row. Now we can begin executing our SQL queries.
```python
c.execute("CREATE TABLE cheeps (name, datetime, cheep)")
```
This creates a table named `cheeps` inside the `temp.db` database with three columns: name, datetime, and cheep. Each cheep will need to have this information. Cool! Now let's try and add a cheep!
```python
c.execute("INSERT INTO cheeps VALUES ('richie', '100', 'Hello world!')")
```
This creates a cheep by the user `richie` with the text `Hello World!`, and that this cheep was created `100` seconds after January 1, 1970 (This is convention for how Python handles time.).

Let's double check that this works. Now we can read from the database and we should be able to see our cheep!
```python
c.execute("SELECT * FROM cheeps")
print(c.fetchall())
```
Now let's commit (save) the changes and close the connection.
```python
conn.commit()
conn.close()
```
Now save the file and run it by doing `python init_db.py`. It should create the `cheeps.db` file and print out something like `[(u'richie', u'100', u'Hello world!')]` to show that reading from the database was successful.

Awesome! Hopefully now you have a basic idea of how sqlite works. Now let's integrate it into our site. Read this short guide in the Flask documentation: [Using SQLite 3 with Flask](http://flask.pocoo.org/docs/patterns/sqlite3/)

Let's steal the code they have in the beginning to get and close the database. We'll add this to our `server.py` file. We'll have to replace their call to `connect_to_database` to connect to our database. Also add in the necessary imports, including the `time` module, which we will be using soon. The top of your `server.py` file should look something like this.

```python
import sqlite3
import time
from flask import Flask, request, g

app = Flask(__name__)
DATABASE = 'cheeps.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
```

Now we can write a few more helper functions to make it easier to interact with the database.
```python
def db_read_cheeps():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM cheeps")
    return cur.fetchall()
```
This (as the function name suggests) reads the cheeps from the database. The function `fetchall` returns them as a list.
```python
def db_add_cheep(name, cheep):
    cur = get_db().cursor()
    t = str(time.time())
    cheep_info = (name, t, cheep)
    cur.execute("INSERT INTO cheeps VALUES (?, ?, ?)", cheep_info)
    get_db().commit()
```
Here we are using the `time` function in the `time` module to get the timestamp for the cheep. This gives us the number of seconds since the epoch (January 1, 1970). The `execute` function also allows us to pass in a tuple, so we can add in question marks in the query string and they will automatically get filled with the data in our `cheep_info` tuple. Finally, after we insert our cheep into the database, we need to commit the changes.

Now that we have all the database logic, we can add it into our route functions. We want all the most recent cheeps to appear on the home page, so the `hello` function should use the `db_read_cheeps` function to display the list of cheeps. Before we do the logic to display the cheeps, let's first double check that this works by simply printing out the cheeps.
```python
@app.route("/")
def hello():
    cheeps = db_read_cheeps()
    print(cheeps)
    return app.send_static_file('index.html')
```
This won't change anything when you visit your homepage, but if you check your terminal window running the server, you should see the list of cheeps getting printed out. You should have one cheep in there if you ran the `init_db.py` script. Something like this.
```
(venv)Richies-MacBook-Air:cheeper richzeng$ python server.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
[(u'richie', u'100', u'Hello world!')]
127.0.0.1 - - [22/Sep/2013 17:45:53] "GET / HTTP/1.1" 304 -
```
Now we need to add in logic to save the cheeps once we submit the form. For that, we'll need to edit the `receive_cheap` function. Remember the `request.form`? That is basically a dictionary containing all the data we submitted in the form. We'll need to grab that data and pass it into our `db_add_cheep` function.
```python
@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    db_add_cheep(request.form['name'], request.form['cheep'])
    return "Success!"
```
That should be everything you need to hook up to your database! Let's make sure it works! Add a tweet using the form on your homepage. It should take you to the page that says "Success!". Now, when you go back to the homepage and check your terminal window, you should see more cheeps getting printed out.

Awesome! The database is hooked up and ready to go.

Step 9: Displaying our cheeps
===========================
Even though the database is showing up, nothing is showing up on our page yet! That's because we're still serving a static html page. We need to write up a template. Don't worry, it's not too bad. Hopefully you remember what you read in the flask quickstart guide earlier, if not check out the [Rendering Templates](http://flask.pocoo.org/docs/quickstart/#rendering-templates) section again.

There are many templating languages out there, each with a slightly different syntax, but their use is basically the same. Think about what a Facebook profile looks like. Every user has a different Facebook profile: different photos, different friends, different posts. But it would be a pain of Facebook had to make a new static HTML page for each user. Instead, you'll notice that every Facebook profile has a the same basic structure and design. The cover photo is on the top, the profile picture is in the top left, and the wall goes down the middle of the profile. The goal of a templating language is to establish this basic structure, and then leave parts of it ready to be filled in based on the URL and any options you pass in.

The templating language we're going to be using is called Jinja. It comes built in with Flask and is maintained by the same group that maintains Flask. You can learn more about it [here](http://jinja.pocoo.org/docs/). We're going to use it in a pretty basic way for now.

First off, we need to make some changes to our `server.py` file to work with Jinja. Import `render_template` from flask. Your imports should look like this now.
```python
import sqlite3
import time
from flask import Flask, g, request, render_template
````
Now replace `send_static_file` with `render_template` inside of the `hello` function. Now it should look like this.
```python
@app.route("/")
def hello():
    cheeps = db_read_cheeps()
    print(cheeps)
    return render_template('index.html')
```
But wait, if you try to visit your homepage right now it won't show up! The problem now is that `render_template` looks for a folder called `templates` for all of your template files. Right now our HTML file is in `static/index.html`! Create a folder called `templates` and copy/move `index.html` into it. Now your original homepage should appear again.

So how does the template get the information from our server? Conveniently, `render_template` handles that for you! Simply pass in a keyword argument into your call to `render_template`.
```python
    return render_template('index.html', cheeps=cheeps)
```
Now we can access the name `cheeps` from our `index.html` file. Take a glance at the [Template Designer Documentation](http://jinja.pocoo.org/docs/templates/). Lets `index.html` it and have it display our first cheep. Remember, a cheep is a tuple with three elements (name, time, cheep), and `cheeps` is a list of them. Find the div with the id `"feed"` and insert the following.
```html
<div id="feed">
    <h2> Cheeps </h2>
    <div class="cheep">
        <b>{{ cheeps[0][0] }}</b>
        <p>{{ cheeps[0][2] }}</p>
    </div>
</div>
```
But we don't want to show only ONE cheep, but we want to be able to list all of them. How do we do that? Well, with a for loop of course! 
```html
<div id="feed">
    <h2> Cheeps </h2>
    {% for cheep in cheeps %}
    <div class="cheep">
        <b>{{ cheep[0] }}</b>
        <p>{{ cheep[2] }}</p>
    </div>
    {% endfor %}
</div>
```
Now it should list all your cheeps!

One more thing, let's remove that dumb "Success!" page after you post a cheep. That would be in your `receive_cheep` function.
Import the function `redirect` from `flask` at the top of your `server.py` file. As you might've guessed, `redirect` will redirect you to a different page, in our case, back to the home page!

Replace the line
```python
return "Success!"
```
with
```python
return redirect("/")
```
Now your site should redirect to the homepage after you post a cheep! 

You've just built your first hack! Show your friends! Tell your mom! Start a billion dollar company!
![](http://i0.kym-cdn.com/photos/images/newsfeed/000/185/885/SANDCASTLES.png?1318627593)

Step 10: Afterward
===========================
Now you've probably gotten a good taste of web development. There are a ton of things you can do from here! Here are a few ideas. We've written a couple mini tutorials that will help you out.

Extending the functionality
* Order tweets by most recent ones first
* Display how long ago the tweet was made
* Make the Cheep post success page redirect to your home.
* Display only the first 10 tweets, with an option to laod more
* Allow image/video cheeps
* Make a user login and registration system
* Add followers
* Add a news feed (ranking tweets, updates in real time)
* [Make your cheeps appear in realtime](https://github.com/sharadmv/beginner-hackjam/tree/master/websocket)

Going further
* [Make your site pretty with Bootstrap](https://github.com/sharadmv/beginner-hackjam/tree/master/bootstrap)
* [Deploy your site to the interwebz with Heroku](https://github.com/sharadmv/beginner-hackjam/tree/master/heroku)
* Make an Android app
* Make an iOS app
