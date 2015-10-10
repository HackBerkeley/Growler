# Welcome to Cal Hacks 2.0!

Welcome to Cal Hacks! If you haven't figured out by now, Cal Hacks is UC Berkeley's annual hella trill hackathon, put on at the California memorial stadium. It's a great place learn, build, and meet other amazing hackers.

If you've never hacked before, don't worry. And if you have hacked before but want to learn how to do web development with python, you're in the perfect place.

This is a guide that will help you through your first hack. We'll be building **Growler**, a Twitter-like communication app for dysfunctional teams, in Flask and Python.

# Step 0: How to get help

If you find yourself getting stuck, don't just stare at the code for an hour. Instead, do the following:

* **Use Google.** Results from [stackoverflow.com](http://stackoverflow.com) are an amazing resource. You get to utilize the knowledge of the global computer science developer community. However, don't just copy-paste answers from the web. Make sure you understand exactly what's going on before you copy-paste anything.
* **Talk to your neighbors.** Working in groups is extremely productive as each of you can fill the gaps of knowledge the others have. Also, it's a good opportunity to **make friends** and find future potential startup cofounders! 
* **Ask people for help.** We have hundreds of mentors, from the community and companies alike, who have volunteered to assist you today. You can ask any of us any question you have. We're nice people. We don't bite.

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

- If you get the error `'pip3' is not recognized as an internal or external command` blah blah blah, you're probably using Windows. You will need to set your PATH variable so that Windows can locate pip3. You will need to add `C:\<Your Python installation directory here>\Scripts\` to your PATH variable. Ask Google, or your neighbor if you're unsure of how to do this, or ask a mentor if you're really stuck.

# Step 3: Get coding

Now that you have Flask installed, you can get started. First, create a folder to hold your new project:

    mkdir growler
    cd growler
    touch server.py

> Note*: If you are on Windows, you don't have the `touch` command. Just open up your text editor and save a file called `server.py` in the `growler` folder.

You just created the `growler` folder and a `server.py` file inside of it. Now open up `server.py` in your favorite text editor.

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
    app.run(debug=True)
```

Copy and paste the example and put it in your `server.py` file. This code imports Flask, creates an application (`app`), and defines a "route" (we'll go over that in a second), and finally starts up the server.

Try running it:

    python3 server.py

If it says something like: `Running on http://127.0.0.1:5000`, then it's working! Test it yourself by going to either `http://localhost:5000` or `http://127.0.0.1:5000` in your favorite browser. It should say "Hello World!".

> *Note*: both `localhost` and `127.0.0.1` are addresses for your own computer and `5000` is the "port" number.

**Future reading**: This is just the tip of the iceberg that is Flask. Check out  [Flask's quick start page](http://flask.pocoo.org/docs/quickstart/) for more examples and to familiarize yourself with the Flask framework. You can stop once you hit [Accessing Request Data](http://flask.pocoo.org/docs/quickstart/#accessing-request-data). Make sure you understand what a route is and how to do routing with Flask.

# Step 4: Creating a user interface

Let's create our home page for Growler. Create a directory in your `growler` directory called `static`. This will be the folder for our *static* files, or the files that don't change and are just retrieved and sent down by Flask when a browser asks for them.

Your project directory should look like this now:
```
growler/
    server.py
    static/
```

Now inside your static folder, create a file called `index.html`. In it, put the following skeleton.
```html
<html>
  <head>
    <title>Growler - better than Twitter</title>
  </head>
  <body>
    Hello World!
  </body>
</html>
```

This is HTML. It's a language that browsers understand and use to render web pages. In HTML files, you define the content and layout of your web page. `index.html` is the name for the default web page that's rendered when you go to a site, so `index.html` will function as the home page. If you open the file in your web browser, you'll get a page that says "Hello World!", and on your tab, it should say what we put into the `<title>` tag.

So now for some user interface design. If you are design inclined yourself, feel free to throw away my suggestions and use your own.

Our Growler webpage should include a glamorous logo and a space to type your growl and growl it to the world. We also need a feed, to display all the growls that have been growled.

First let's add the logo, which will just be really big text. We can do this with `<h1>`. Add an `<h1>` tag into the body of `index.html`, which will be our logo.

```html
...
<body>
  <h1>Growler</h1>
</body>
...
```

Now let's add the form to write and submit your growls. Growls are only 76 characters long, right?

```html
...
<body>
  <h1>Growler</h1>
  <form>
    Name:
    <input name="name" type="text" /> 
    Growl:
    <input name="growl" type="text" maxlength="76" />
    <input type="submit" />
  </form>
</body>
...
```

Awesome! Our awesome, beautiful user interface is almost done. Let's now add a container (in HTML, this is known as a `div`) for the Growler feed to appear, just before the closing `body` tag.

```html
...
  </form>
  <div id="feed">
  </div>
</body>
...
```
Cool! This is possibly the best UI I've ever designed.

**Future reading**: Now, I suggest reading up on the basics of HTML. Make sure you understand how to create forms. Here's a [Codecademy tutorial](http://www.codecademy.com/courses/web-beginner-en-Vfmnp/0/2) on creating web forms! If you feel that this UI needs improvement, make it look as nice as you want. Look into using [*CSS*](https://www.codecademy.com/courses/css-coding-with-style/0/1).

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

Refresh your browser so that `localhost:5000` is reloaded. You should see your changes. If you get a "connection not found" error, check the console to ensure `server.py` is still running.

Woot! Your site should now have a basic form for submitting growls showing. It doesn't actually do anything yet. We're about to fix that.

# Step 6: Sending requests to Flask

Let's quickly establish the notion of a *front end* and a *back end*.

- **Front end**: what the "client," or web browser sees. In our case, files in `static/` are the front end.
- **Back end**: the application that handles storing, manipulating, and sending data back to the front end. In our case, `server.py` is the back end, so far.

Right now, Flask just spits out our `index.html` file. What we now want to do is to send the data from your web form to Flask. In `index.html`, add an `action` attribute and a `method` attribute with the following values to your form.

```html
...
<form action='/api/growl' method="POST">
  Name:
  <input name="name" type="text" /> 
  Growl:
  <input name="growl" type="text" maxlength="76" />
  <input type="submit" />
</form>
```

- The form's **action** is the URL to which it submits its data. When you click the submit button, the browser gathers all the form data and sends it to the given URL. We're sending the form data to the `/api/growl` URL.
- The form's **method** is the HTTP method, which can be GET, POST, or some other more obscure methods. Essentially, a POST request means that we want to *store* data on the server.

Now that we send the data, we need to handle the data we receive in Flask.  Let's go back to `server.py`.

First, add `request` to our list of imports from `flask`.
```python
from flask import Flask, request
...
```

The request object allows us to get data and information about incoming HTTP requests.

Now we need to create a route for `/api/growl` to actually receive the data.

Add the following method into your `server.py`, underneath the `hello()` function and before the `if __name__ == "__main__":`. I'll explain what it does in a bit.

```python
@app.route("/api/growl", methods=["POST"])
def receive_growl():
    print(request.form)
    return "Success!"
```

> Note: at this point, you might be wondering what the `@app.route(...)` above the function definition does. It's what we call a function *decorator*. Decorators augments the behavior of a function. The `app.route` decorator makes your ordinary Python function into a server route. Pretty amazing! If you want to read more about decorators, check out [this link](http://www.shutupandship.com/2012/01/python-decorators-i-functions-that.html).

In this new code we just added, we're adding a new route for `/api/growl`, which would correspond to the url `localhost:5000/api/growl`. We make sure it handles POST requests by saying so. In the function body itself, we're just printing out the data sent up by the form (for debugging purposes) and then returning a success message.

To test this out, restart your server and go to `localhost:5000`. Fill out your form with some data and hit the submit button. It should take you to a page that says "Success!" on it. Now look back at your server log (your terminal where you started the server). It should say something like: 
```
ImmutableMultiDict([('growl', 'testing 123'), ('name', 'bob jones')])
```

Don't worry exactly what this means. Just make sure it is filled with the data you submitted.

# Step 7: Storing our growls

So at this point, our HTML page should be sending successful requests to the Flask server, but our growls aren't showing up on our home page!

Our job will now be to store the growls that are sent up to Flask. We'll do this with a *database*. A database allows us to store data on the hard disk and retrieve it later.

This is a very general pattern for web applications. The user will input some data on the front end. The data will be sent up via an HTTP request to the web server. The web server will then store the data in some sort of database. 

Later, when the user wants to see their data, they'll request data from the web server via HTTP request, the server will ask the database for the data, then send it back down in the HTTP response.

We'll be using the `sqlite3` database to store our growls. It's conveniently packaged with Python, so we don't need to install anything!

So what's `sqlite3`? Well, you might have heard of SQL before. It stands for *Structured Query Language* and it's a language you use to ask, or query, a database for data. In SQL databases, data is organized into *tables*, which have rows and columns. `sqlite3` is just an example of a SQL database.

As mentioned above, a database is a collection of tables, kind of like an Excel spreadsheet, where each column is a different piece of information that an entry needs, and each row is an entry in the table.

Let's play with sqlite a bit first. Make a file called `init_db.py` in your `growler` folder. Put the following in.
```python
import sqlite3
conn = sqlite3.connect('growls.db')
```

This imports the sqlite package and opens a connection to the database file named `growls.db`. If the file doesn't exist, sqlite will create it automatically.
```python
c = conn.cursor()
```
We'll go more into detail on this later. A cursor basically points to a specific row in the database, which allows a programmer to make changes row by row. Now we can begin executing our SQL queries.
```python
c.execute("CREATE TABLE IF NOT EXISTS growls (name, datetime, growl)")
```
This creates a new table named `growls` inside the `growls.db` database with three columns: name, datetime, and growl. (If you rerun this, the `IF NOT EXISTS` makes sure you don't overwrite your data so far.) Each growl will need to have this information. Cool! Now let's try and add a growl!

```python
c.execute("INSERT INTO growls VALUES ('oski', '100', 'Hello Cal Hacks!')")
```

This creates a growl by the user `oski` with the text `Hello Cal Hacks!`, and that this growl was created `100` seconds after January 1, 1970 (This is convention for how Python handles time.).

Let's double check that this works. Now we can read from the database and we should be able to see our growl!
```python
c.execute("SELECT * FROM growls")
print(c.fetchall())
```
Now let's commit (save) the changes and close the connection.
```python
conn.commit()
conn.close()
```
Now save the file and run it by doing `python3 init_db.py`. It should create the `growls.db` file and print out something like `[('bob', '100', 'Hello world!')]` to show that reading from the database was successful. Awesome!

Let's add a databse to our Flask server. We'll add the following code to our `server.py` file. Add in the new Flask imports `g` and the `time` module, which we will be using soon. Let's also make a constant for the name of our databse, so we don't have to repeat the database name everywhere. The top of your `server.py` file should look something like this.

```python
import sqlite3
import time
from flask import Flask, request, g

app = Flask(__name__)
DATABASE = 'growls.db'
```

Then let's add two functions to connect and disconnect from the database inside Flask. This code is borrowed from the Flask documentation, and you don't need to understand it right now.

```python
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
def db_read_growls():
    c = get_db().cursor()
    c.execute("SELECT * FROM growls")
    return cur.fetchall()
```
This (as the function name suggests) reads the growls from the database. The function `fetchall` returns them as a list.
```python
def db_add_growl(name, growl):
    c = get_db().cursor()
    t = str(time.time())
    growl_info = (name, t, growl)
    c.execute("INSERT INTO growls VALUES (?, ?, ?)", growl_info)
    get_db().commit()
```
Here we are using the `time` function in the `time` module to get the timestamp for the growl. This gives us the number of seconds since the epoch (January 1, 1970). The `execute` function also allows us to pass in a tuple, so we can add in question marks in the query string and they will automatically get filled with the data in our `growl_info` tuple. Finally, after we insert our growl into the database, we need to commit the changes.

Now that we have all the database logic, we can add it into our route functions. We want all the most recent growls to appear on the home page, so the `hello` function should use the `db_read_growls` function to display the list of growls. Before we do the logic to display the growls, let's first double check that this works by simply printing out the growls.
```python
@app.route("/")
def hello():
    growls = db_read_growls()
    print(growls)
    return app.send_static_file('index.html')
```
Reload your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). Nothing will have changed, but if you check your terminal window running the server, you should see the list of growls getting printed out. You should have one growl in there if you ran the `init_db.py` script. Something like this:
```
 * Running on http://127.0.0.1:5000/
[('oski', '100', 'Hello Cal Hacks!')]
127.0.0.1 - - [16/Jul/2014 23:10:15] "GET / HTTP/1.1" 200 -
```
Now we need to add in logic to save the growls once we submit the form. For that, we'll need to edit the `receive_growl` function. Remember the `request.form`? That is basically a dictionary containing all the data we submitted in the form. We'll need to grab that data and pass it into our `db_add_growl` function.
```python
@app.route("/api/growl", methods=["POST"])
def receive_growl():
    print(request.form)
    db_add_growl(request.form['name'], request.form['growl'])
    return "Success!"
```
That should be everything you need to hook up to your database! Let's make sure it works! Add a tweet using the form on your homepage. It should take you to the page that says "Success!". Now, when you go back to the homepage, refresh your browser, and check your terminal window, you should see more growls getting printed out.

If SQL at all seems a bit intimidating for you, don't worry. There are better an eaisier solutions for databses (which unfortunately may take too long to explain in depth in this workshop.) But feel free to google and ask about SQLAlchemy and MongoDB. We might also have sponsor workshops on those topics, so check in the Cal Hacks group.

Awesome! The database is hooked up and ready to go.

**Future reading**: We glossed over sqlite and SQL, only covering what was necessary to build Growler. To learn more about it, read this short guide in the Flask documentation: [Using SQLite 3 with Flask](http://flask.pocoo.org/docs/patterns/sqlite3/)

# Step 8: Displaying our growls

Even though the database is showing up, nothing is showing up on our page yet! That's because we're still serving a static html page. We need to write up a *template*.

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
    growls = db_read_growls()
    print(growls)
    return render_template('index.html')
```
But wait, if you try to visit your homepage right now it won't show up! The problem now is that `render_template` looks for a folder called `templates` for all of your template files. Right now our HTML file is in `static/index.html`! Rename the `static` folder and call it `templates`. Now your original homepage should appear again.

So how does the template get the information from our server? Conveniently, `render_template` handles that for you! Simply pass in a keyword argument into your call to `render_template`.
```python
    return render_template('index.html', growls=growls)
```
Now we can access `growls` from our `index.html` file. Lets edit `index.html` and have it display our first growl. Remember, a growl is a tuple with three elements (name, time, growl), and `growls` is a list of them. Find the `div` container with the id `"feed"` and insert the following.
```html
<div id="feed">
    <h2>Growls</h2>
    <div class="growl">
        <b>{{ growls[0][0] }}</b>
        <p>{{ growls[0][2] }}</p>
    </div>
</div>
```
But we don't want to show only ONE growl, but we want to be able to list all of them. How do we do that? Well, with a for loop of course!
```html
<div id="feed">
    <h2> Hakks </h2>
    {% for growl in growls %}
    <div class="growl">
        <b>{{ growl[0] }}</b>
        <p>{{ growl[2] }}</p>
    </div>
    {% endfor %}
</div>
```
Now it should list all your growls!

One more thing, let's change that "Success!" page after you post a growl. That would be in your `receive_growl` function.

Let's go back to server.py. Import the function `redirect` from `flask` at the top of your `server.py` file. As you might've guessed, `redirect` will redirect you to a different page, in our case, back to the home page!

```python
import sqlite3
import time
from flask import Flask, g, request, render_template
```

Now, inside your `receive_growl()` function, replace the line
```python
return "Success!"
```
with
```python
return redirect("/")
```
Now your site should redirect to the homepage after you post a growl!

**Future reading**: Take a glance at the [Template Designer Documentation](http://jinja.pocoo.org/docs/templates/) to learn more about how to use templates in Flask.

# Step 9: Make this pretty

We've done a lot here. But let's make it look a little better.

First, go back to the **static** folder and make a file called `style.css`

This should contain some basic css to make the app a bit prettier:

```css
html {
  background-color: #AAF0D1;
}

body {
  font-family: sans-serif;
  max-width: 500px;
  margin: auto;
  padding: 20px;
  margin-top: 10px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
```
What this does is it takes the body and puts it in the center with `margin: auto`

The rest of the code limits the size of the body, makes sure the background is white, positions it, and then puts a nice subtle drop shadow on it. This is pretty self explanatory.

In addition, the background color has been changed to a nice a lovely **menthe**.

If you want to understand or learn CSS more, check out [this Codecademy tutorial](https://www.codecademy.com/courses/css-coding-with-style/0/1) or feel free to ask a mentor! This example is so you know how to include the CSS made by the frontend person on your team (if you have one), so we won't explore CSS here.

Finally, to finish off, let's link this css file in our template by adding this line of code after the `</title>` tag in your main template:

```html
...
  <title>Growler - better than Twitter</title>
  <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
</head>
...
```

You've just built your first hack! Show your friends! Tell your mom! Start a billion dollar company!
![](http://i0.kym-cdn.com/photos/images/newsfeed/000/185/885/SANDCASTLES.png?1318627593)

# Step 10: Now what?

Now you've gotten a taste of backend development. Welcome to the wonderful world. There are a ton of things you can do from here! Here are a few ideas.

### Easy tweaks
* Order tweets by most recent ones first
* Display how long ago the tweet was made
* Make your site pretty by adding Bootstrap CSS
* People can submit Growls that have no content or user. Make sure that growls are well-formed.

### Medium difficulty
* Display only the first 10 tweets, with an option to load more
* Allow image/video growls
* Deploy your site to the Internet with Heroku

### Challenging exercises
* Make a user login and registration system
* Add upvotes. Make reddit!
* Add followers
* Add a news feed (ranking tweets, updates in real time)
* Make a billion dollars by transforming this hack into a company
