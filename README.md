# Welcome to HackJam Spring 2015

Welcome to HackJam! If you haven't figured out by now, HackJam is an awesome low pressure hella chill hackathon that the amazing group Hackers @ Berkeley puts on once a semester. It's a great place to work on a side project and network with other amazing hackers.

If you've never hacked before, don't worry. And if you have hacked before but want to learn how to do web development with python, you're in the perfect place.

This is a guide that will help you through your first hack. We'll be building **Hakker**, a simple twitter like communication app for dysfunctional teams, in flask/python.

# Step 0: How to get help

If you find yourself getting stuck, don't just stare at the code for an hour. Instead, do the following:

* **Use Google.** Results from [stackoverflow.com](http://stackoverflow.com) are an amazing resource. You get to utilize the knowledge of the global computer science developer community. However, don't just copy-paste answers from the web. Make sure you understand exactly what's going on before you copy-paste anything.
* **Ask your neighbors.** Working in groups is extremely productive as each of you can fill the gaps of knowledge the others have. Also, it's a good opportunity to **make friends** and find future potential startup cofounders! 
* **Ask H@B members for help.** Several H@B members have volunteered to assist people today. But you can just ask any of us to be honest. Well, err most of us. We're nice people. We don't bite. Here are just a few of them.
 <table><tr><td><img src="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-xfp1/v/t1.0-9/10885498_877064285678413_1508690135448109619_n.jpg?oh=206866b690a8b7c102133473370e024b&oe=55896EBF&__gda__=1431147062_291e876cb41f9d56acf62322f58456a7" width="200" height="auto"></td>
 <td><img src="https://scontent-sjc.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/426802_3271389590516_1481383110_n.jpg?oh=2cc91f2c3848877f197bbf35a75e8dab&oe=55488DCF" width="200" height="auto"></td>
 <td><img src="https://scontent-sjc.xx.fbcdn.net/hphotos-xpf1/t31.0-8/51813_4726469958853_780877942_o.jpg" width="200" height="auto"></td>
 <td><img src="https://scontent-sjc.xx.fbcdn.net/hphotos-xpa1/l/t31.0-8/10849013_1568766236703666_7856351810450671921_o.jpg" width="200" height="auto"></td>
 </tr><tr><td>Smitha Milli</td><td>Mitchell Karchemsky</td><td>Brian Chu</td><td>David Bui</td></tr></table>

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

If you're on OSX, make sure you have [XCode and Xcode command line tools installed](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)

Flask is a web framework for Python. It makes it really easy to write web apps. Let's get it installed.

In your command line, type

    pip3 install flask

- If you get the error `'pip3' is not recognized as an internal or external command` blah blah blah, you're probably using Windows. You will need to set your PATH variable so that Windows can locate pip3. You will need to add `C:\<Your Python installation directory here>\Scripts\` to your PATH variable. Ask Google or your neighbor if you're unsure of how to do this, or ask a H@B officer if you're really stuck.

# Step 3: Get coding

Now that you have Flask installed, you can get started. First, create a folder to hold your new project:

    mkdir hakker
    cd hakker
    touch server.py

- If you are on Windows, you don't have the `touch` command. Just open up your text editor and save a file called `server.py` in the `hakker` folder.

You just created the `hakker` folder and a `server.py` file inside of it. Now open up `server.py` in your favorite text editor.

Okay, so let's get started with Flask. 

First, what exactly is a web framework? When a person goes to a website, they send what's called an *HTTP request* to that website, asking for the site's content. Our web framework, Flask, will handle requests that are sent to us, and send back our site's content via an *HTTP response*.

Let's try building Hello World, but with a twist.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Go Bears!"

if __name__ == "__main__":
    app.run()
```

Copy and paste the example and put it in your `server.py` file. This code imports Flask, creates an application (`app`), and defines a "route" (we'll go over that in a second), and finally starts up the server.

Try running it:

    python3 server.py

If it says something like: `Running on http://127.0.0.1:5000`, then it's working! Test it yourself by going to either `http://localhost:5000` or `http://127.0.0.1:5000` in your favorite browser. It should say "Hello World!".

> *Note*: both `localhost` and `127.0.0.1` are addresses for your own computer and `5000` is the "port" number.

Now that you have this working, please go through the examples on the Flask [quick start page](http://flask.pocoo.org/docs/quickstart/) and familiarize yourself with the Flask framework. You can stop once you hit [Accessing Request Data](http://flask.pocoo.org/docs/quickstart/#accessing-request-data). Make sure you understand what a route is and how to do routing with Flask. Hint: decorators.

# Step 4: Creating a user interface

Let's create our home page for Hakker. Create a directory in your `hakker` directory called `static`. This will be the folder for our *static* files, or the files that don't change and are just retrieved and sent down by Flask when a browser asks for them.

Your project directory should look like this now:
```
hakker/
    server.py
    static/
```

Now inside your static folder, create a file called `index.html`. In it, put the following skeleton.
```html
<html>
  <head>
    <title>Hakker - better than Twitter</title>
  </head>
  <body>
    Hello World!
  </body>
</html>
```

This is HTML. It's a language that browsers understand and use to render web pages. In HTML files, you define the content and layout of your web page. `index.html` is the name for the default web page that's rendered when you go to a site, so `index.html` will function as the home page.

If you open the file in your web browser, you'll get a page that says "Hello World!", and on your tab, it should say what we put into the `<title>` tag.

Now, I suggest reading up on the basics of HTML. Make sure you understand how to create forms. Here's a [Codecademy tutorial](http://www.codecademy.com/courses/web-beginner-en-Vfmnp/0/2) on creating web forms!

So now for some user interface design. If you are design inclined yourself, feel free to throw away my suggestions and use your own.

Our Hakker webpage should include a glamorous logo and a space to type your hakk and hakk it to the world. We also need a feed, to display all the hakks that have been hakked.

First let's add the logo, which will just be really big text. We can do this with the `<h1>`. Add an `<h1>` tag into the body of `index.html`, which will be our logo.

```html
...
<body>
  <h1>Hakker</h1>
</body>
...
```

Now let's add the form to write and submit your hakks. Hakks are only 76 characters long, right?

```html
...
<body>
  <h1>Hakker</h1>
  <form>
    Name:
    <input name="name" type="text" /> 
    Hakk:
    <input name="hakk" type="text" maxlength="76" /> 
    <input type="submit" />
  </form>
</body>
...
```

Awesome! Our awesome, beautiful user interface is almost done. Let's now add a container (in HTML, this is known as a `div`) for the Hakker feed to appear, just before the closing `body` tag.

```html
...
  </form>
  <div id="feed">
  </div>
</body>
...
```
Cool! This is possibly the best UI I've ever designed. If you feel that it needs improvement, make it look as pretty as you want. Look into using *CSS*.

# Step 5: Serving static webpages

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

Stop your server using Ctrl-C and start it again (`python3 server.py`), and then go to `localhost:5000`.

> *Note*: You can see your changes to `index.html` immediately by just refreshing, but you need to restart your server (using Ctrl-C) every time you modify `server.py`.

Woot! Your site should now have a basic form for submitting hakks showing.

# Step 6: Sending requests to Flask

Let's quickly establish the notion of a *front end* and a *back end*.

- **Front end**: what the "client," or web browser sees. In our case, files in `static/` are the front end.
- **Back end**: the application that handles storing, manipulating, and sending data back to the front end. In our case, `server.py` is the back end, so far.

Right now, Flask just spits out our `index.html` file. What we now want to do is to send the data inputted into your web form to Flask. In `index.html`, add an `action` attribute and a `method` attribute with the following values to your form.

```html
...
<form action='/api/hakk' method="POST">
  Name:
  <input name="name" type="text" /> 
  Hakk:
  <input name="hakk" type="text" maxlength="76" /> 
  <input type="submit" />
</form>
```

- The form's **action** is the URL to which it submits its data. When you click the submit button, the form gathers all its data and sends it to the given URL. We're sending the form data to the `/api/hakk` URL.
- The form's **method** is the HTTP method, which can be GET, POST, or some other more obscure methods. Essentially, a POST request means that we want to *store* data on the server.

Now that we send the data, we need to handle the data we receive in Flask.  Let's go back to `server.py`.

First, add `request` to our list of imports from `flask`.
```python
from flask import Flask, request
...
```

The request object allows us to get data and information about incoming HTTP requests.

Now we need to create a route for `/api/hakk` to actually receive the data.

Add the following method into your `server.py` before the `if __name__ == "__main__":`. I'll explain what it does in a bit.

```python
@app.route("/api/hakk", methods=["POST"])
def receive_hakk():
    print(request.form)
    return "Success!"
```

> Note: at this point, you might be wondering what the `@app.route(...)` above the function definition does. It's what we call a function *decorator*. Decorators augments the behavior of a function. The `app.route` decorator makes your ordinary Python function into a server route. Pretty amazing! If you want to read more about decorators, check out [this link](http://www.shutupandship.com/2012/01/python-decorators-i-functions-that.html).

In this new code we just added, we're adding a new route for `/api/hakk`, which would correspond to the url `localhost:5000/api/hakk`. We make sure it handles POST requests by saying so. In the function body itself, we're just printing out the data sent up by the form (for debugging purposes) and then returning a success message.

To test this out, restart your server and go to `localhost:5000`. Fill out your form with some data and hit the submit button. It should take you to a page that says "Success!" on it. Now look back at your server log (your terminal where you started the server). It should say something like: 
```
ImmutableMultiDict([('hakk', 'testing 123'), ('name', 'bob jones')])
```

Don't worry exactly what this means. Just make sure it is filled with the data you submitted.

# Step 7: Storing our hakks

So at this point, our HTML page should be sending successful requests to the Flask server, but our hakks aren't showing up on our home page!

Our job will now be to store the hakks that are sent up to Flask. We'll do this with a *database*. A database allows us to store data on the hard disk and retrieve it later.

This is a very general pattern for web applications. The user will input some data on the front end. The data will be sent up via an HTTP request to the web server. The web server will then store the data in some sort of database. 

Later, when the user wants to see their data, they'll request data from the web server via HTTP request, the server will ask the database for the data, then send it back down in the HTTP response.

We'll be using the `sqlite3` database to store our hakks. It's conveniently packaged with Python, so we don't need to install anything!

So what's `sqlite3`? Well, you might have heard of SQL before. It stands for *Structured Query Language* and it's a language you use to ask, or query, a database for data. In SQL databases, data is organized into *tables*, which have rows and columns. `sqlite3` is just an example of a SQL database.

As mentioned above, a database is a collection of tables, kind of like an Excel spreadsheet, where each column is a different piece of information that an entry needs, and each row is an entry in the table.

Let's play with sqlite a bit first. Make a file called `init_db.py` in your `hakker` folder. Put the following in.
```python
import sqlite3
conn = sqlite3.connect('hakks.db')
```

This imports the sqlite package and opens a connection to the database file named `hakks.db`. If the file doesn't exist, sqlite will create it automatically.
```python
c = conn.cursor()
```
We'll go more into detail on this later. A cursor basically points to a specific row in the database, which allows a programmer to make changes row by row. Now we can begin executing our SQL queries.
```python
c.execute("CREATE TABLE hakks (name, datetime, hakk)")
```
This creates a table named `hakks` inside the `hakks.db` database with three columns: name, datetime, and hakk. Each hakk will need to have this information. Cool! Now let's try and add a hakk!
```python
c.execute("INSERT INTO hakks VALUES ('bob', '100', 'Hello world!')")
```
This creates a hakk by the user `bob` with the text `Hello World!`, and that this hakk was created `100` seconds after January 1, 1970 (This is convention for how Python handles time.).

Let's double check that this works. Now we can read from the database and we should be able to see our hakk!
```python
c.execute("SELECT * FROM hakks")
print(c.fetchall())
```
Now let's commit (save) the changes and close the connection.
```python
conn.commit()
conn.close()
```
Now save the file and run it by doing `python3 init_db.py`. It should create the `hakks.db` file and print out something like `[('bob', '100', 'Hello world!')]` to show that reading from the database was successful.

Awesome! Hopefully now you have a basic idea of how sqlite works. Now let's integrate it into our site. Read this short guide in the Flask documentation: [Using SQLite 3 with Flask](http://flask.pocoo.org/docs/patterns/sqlite3/)

Let's steal the code they have in the beginning to get and close the database. We'll add this to our `server.py` file. We'll have to replace their call to `connect_to_database` to connect to our database. Also add in the necessary imports, including the `time` module, which we will be using soon. The top of your `server.py` file should look something like this.

```python
import sqlite3
import time
from flask import Flask, request, g

app = Flask(__name__)
DATABASE = 'hakks.db'

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
def db_read_hakks():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM hakks")
    return cur.fetchall()
```
This (as the function name suggests) reads the hakks from the database. The function `fetchall` returns them as a list.
```python
def db_add_hakk(name, hakk):
    cur = get_db().cursor()
    t = str(time.time())
    hakk_info = (name, t, hakk)
    cur.execute("INSERT INTO hakks VALUES (?, ?, ?)", hakk_info)
    get_db().commit()
```
Here we are using the `time` function in the `time` module to get the timestamp for the hakk. This gives us the number of seconds since the epoch (January 1, 1970). The `execute` function also allows us to pass in a tuple, so we can add in question marks in the query string and they will automatically get filled with the data in our `hakk_info` tuple. Finally, after we insert our hakk into the database, we need to commit the changes.

Now that we have all the database logic, we can add it into our route functions. We want all the most recent hakks to appear on the home page, so the `hello` function should use the `db_read_hakks` function to display the list of hakks. Before we do the logic to display the hakks, let's first double check that this works by simply printing out the hakks.
```python
@app.route("/")
def hello():
    hakks = db_read_hakks()
    print(hakks)
    return app.send_static_file('index.html')
```
Restart your server and then visit your website. Nothing will have changed, but if you check your terminal window running the server, you should see the list of hakks getting printed out. You should have one hakk in there if you ran the `init_db.py` script. Something like this:
```
 * Running on http://127.0.0.1:5000/
[('bob', '100', 'Hello world!')]
127.0.0.1 - - [16/Jul/2014 23:10:15] "GET / HTTP/1.1" 200 -
```
Now we need to add in logic to save the hakks once we submit the form. For that, we'll need to edit the `receive_cheap` function. Remember the `request.form`? That is basically a dictionary containing all the data we submitted in the form. We'll need to grab that data and pass it into our `db_add_hakk` function.
```python
@app.route("/api/hakk", methods=["POST"])
def receive_hakk():
    print(request.form)
    db_add_hakk(request.form['name'], request.form['hakk'])
    return "Success!"
```
That should be everything you need to hook up to your database! Let's make sure it works! Add a tweet using the form on your homepage. It should take you to the page that says "Success!". Now, when you go back to the homepage, refresh your browser, and check your terminal window, you should see more hakks getting printed out.

If SQL at all seems a bit intimidating for you, don't worry. There are better an eaisier solutions for databses (which unfortunately may take too long to explain in depth in this workshop.) But feel free to google and ask about SQLAlchemy and MongoDB.

Awesome! The database is hooked up and ready to go.

# Step 8: Displaying our hakks

Even though the database is showing up, nothing is showing up on our page yet! That's because we're still serving a static html page. We need to write up a *template*. Don't worry, it's not too bad. Hopefully you remember what you read in the flask quickstart guide earlier, if not check out the [Rendering Templates](http://flask.pocoo.org/docs/quickstart/#rendering-templates) section again.

What's a template? Think about what a Facebook profile looks like. Every user has a different Facebook profile: different photos, different friends, different posts. But it would be a pain of Facebook had to make a new static HTML page for each user. Instead, you'll notice that every Facebook profile has a the same basic structure and design. The cover photo is on the top, the profile picture is in the top left, and the wall goes down the middle of the profile. The goal of a templating language is to establish this basic structure, and then leave parts of it ready to be filled in based on the URL and any options you pass in.

Let's write a template. First, we'll need to import `render_template` from flask. Your imports should look like this now.
```python
import sqlite3
import time
from flask import Flask, g, request, render_template
```
Now replace `send_static_file` with `render_template` inside of the `hello` function. Now it should look like this.
```python
@app.route("/")
def hello():
    hakks = db_read_hakks()
    print(hakks)
    return render_template('index.html')
```
But wait, if you try to visit your homepage right now it won't show up! The problem now is that `render_template` looks for a folder called `templates` for all of your template files. Right now our HTML file is in `static/index.html`! Rename the `static` folder and call it `templates`. Now your original homepage should appear again.

So how does the template get the information from our server? Conveniently, `render_template` handles that for you! Simply pass in a keyword argument into your call to `render_template`.
```python
    return render_template('index.html', hakks=hakks)
```
Now we can access the name `hakks` from our `index.html` file. Take a glance at the [Template Designer Documentation](http://jinja.pocoo.org/docs/templates/). Lets edit `index.html` and have it display our first hakk. Remember, a hakk is a tuple with three elements (name, time, hakk), and `hakks` is a list of them. Find the `div` container with the id `"feed"` and insert the following.
```html
<div id="feed">
    <h2> Hakks </h2>
    <div class="hakk">
        <b>{{ hakks[0][0] }}</b>
        <p>{{ hakks[0][2] }}</p>
    </div>
</div>
```
But we don't want to show only ONE hakk, but we want to be able to list all of them. How do we do that? Well, with a for loop of course! 
```html
<div id="feed">
    <h2> Hakks </h2>
    {% for hakk in hakks %}
    <div class="hakk">
        <b>{{ hakk[0] }}</b>
        <p>{{ hakk[2] }}</p>
    </div>
    {% endfor %}
</div>
```
Now it should list all your hakks!

One more thing, let's remove that dumb "Success!" page after you post a hakk. That would be in your `receive_hakk` function.
Import the function `redirect` from `flask` at the top of your `server.py` file. As you might've guessed, `redirect` will redirect you to a different page, in our case, back to the home page!

Replace the line
```python
return "Success!"
```
with
```python
return redirect("/")
```
Now your site should redirect to the homepage after you post a hakk! 

# Step 9: Make this pretty

We've done a lot here. But let's make it look a little better.

First, go back to the **static** folder and make a file called `style.css`

This should contain some basic css to make the app a bit prettier:

```css
html {
  background-color: #AAF0D1;
}

body {
  font-family: Sans-serif;
  max-width: 500px;
  margin: auto;
  padding: 20px;
  margin-top: 10px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}
```
What this does is it takes the body and puts it in the center with `margin: auto`

The rest of the code limits the size of the body, makes sure the background is white, positions it, and then puts a nice subtle drop shadow on it. This s pretty self explanatory.

In addition, the background color has been changed to a nice a lovely **menthe**.

If you want to understand or learn CSS more feel free to bug **David** or just ask around!

Finally, to finish off, let's link this css file in our template by adding this line of code after the `</title>` tag in your main template:

```html
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
```

You've just built your first hack! Show your friends! Tell your mom! Start a billion dollar company!
![](http://i0.kym-cdn.com/photos/images/newsfeed/000/185/885/SANDCASTLES.png?1318627593)

# Step 10: Now what?

Now you've gotten a taste of web development. Welcome to the wonderful world. There are a ton of things you can do from here! Here are a few ideas.

### Easy tweaks
* Order tweets by most recent ones first
* Add upvotes. Make reddit!
* Display how long ago the tweet was made
* [Make your site pretty with Bootstrap](https://github.com/sharadmv/beginner-hackjam/tree/master/bootstrap)

### Medium difficulty
* Display only the first 10 tweets, with an option to load more
* Allow image/video hakks
* [Make your hakks appear in realtime](https://github.com/sharadmv/beginner-hackjam/tree/master/websocket)

### Challenging exercises
* Make a user login and registration system
* Add followers
* Add a news feed (ranking tweets, updates in real time)
* [Deploy your site to the Internet with Heroku](https://github.com/sharadmv/beginner-hackjam/tree/master/heroku)
* Make a billion dollars by transforming this hack into a company
