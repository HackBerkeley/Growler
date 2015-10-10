This is it, you've spent hours developing your app. You're ready for the world to see it. But is the world ready? Guess we'll have to see. We're going to be deploying your site to the internet!

We're going to be using Heroku, which is a platform that lets you quickly and easily deploy your applications to the web. Let's get started!

Setup
==================
Heroku relies on git, which is a tool that helps you manage the history of changes/updates in your project. If you aren't familiar with version control or git, here are a [good series of videos](http://git-scm.com/videos) that explain what these things are.

If you don't have git installed you can go [here](http://git-scm.com/book/en/Getting-Started-Installing-Git) and follow the instructions for your operating system.

Afterwards, you need to sign up for Heroku and install the tools by following the instructions [here](https://devcenter.heroku.com/articles/quickstart).

Deploying
==================
We honestly can't do much better than the documentation that Heroku provides, but if you need somebody to explain what's going on, don't hesitate to ask a neighbor or a H@B officer!

[Here are the instructions](https://devcenter.heroku.com/articles/getting-started-with-python) for deploying your project to Heroku. You'll notice that we already did some of these steps in the first tutorial. You can actually just run `pip install gunicorn` and then start from the section [Declare process types with Procfile](https://devcenter.heroku.com/articles/getting-started-with-python#declare-process-types-with-procfile). Keep in mind that this guide uses the file `hello.py` for their server, while our file is called `server.py`. Basically our Procfile will say `web: gunicorn server:app` instead of `web: gunicorn hello:app`.

By the time you've gone through these steps, you will have deployed your site to the web! Get on Facebook and message your friends and tell them to user your app! Call your relatives and get them to post some Growls!
