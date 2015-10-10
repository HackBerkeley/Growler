Growler in Realtime
================================

This tutorial is a follow up to the beginner hack. This tutorial will be more about you exploring different technologies and experimenting with them and will involve less sample code than the previous guide.

Let's add realtime functionality to Growler. When anyone makes a Growl, we want it to appear *instantly* on everyone else's page.

This is actually super tricky. Realtime functionality has been prevalent in the web for a very long time, but only recently have technologies come out that have made it practical.

Websockets are a persistent connection between a client and the server that allows bi-directional communication. Before, with old HTTP, we only had the request-response model, where a client had to initiate a connection with server and only expect one response back. With websockets, we can have the server send the client any new information whenever it's ready and the client doesn't have to send a request for it.

There are two portions to websockets: a client and a server. Let's work on the server. 

Step 1: Websocket server
---------------------------

Adding websocket functionality to the server is annoying due to a Flask limitation, but it's still possible using the `gevent` library and the `gevent-websocket` library. Install these with `pip`. (You may be missing some operating system dependencies, such as `libevent`. You'll need to figure out how to install these). Once you have these installed, you'll need to integrate it with your Flask server.

To add websocket functionality to our server, add this to the beginning of your `server.py` file.
```python
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
```

Now replace the end of your file with this:
```python
if __name__ == "__main__":
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
```

This code imports the websockets library and injects the websocket library into Flask.

Here's a quick overview on how to use websockets with your server now.
```python
@app.route('/ws')
def ws():
    if request.environ.get('wsgi.websocket'):
        websocket = request.environ['wsgi.websocket']
        return
    return "No Websocket"
```
This route creates a websocket to the client who made the request to `/ws`. Websockets support several important methods.

* `ws.send(message)` - Sends a string message to the other end of the websocket
* `ws.receive()` - Waits until a string message arrives on the websocket and returns it

With these methods, you can send information back and forth between the client and the server whenever you want to.

Now with this in mind, you have to design a protocol to let everyone on the site know when a growl is sent, and send the growl down to all of them.

Things to consider:
* When a websocket route returns, the websocket is terminated, meaning you have to keep the request alive forever. Consider using a `while True:`.
* You have to maintain a list of everyone's websockets so that you can broadcast the latest growl to everyone via their websocket
* You have to devise some sort of protocol for the client and server to communicate to each other. Websockets support sending strings, so you'll need to organize how you send down information. Consider using `json`.

Step 2: Websocket client
------------------------
Writing the websocket client will be very much different than how the server was structured, but the nice part is that most of the logic has been written already. By this point, you should have a Flask server that has a route for websockets and broadcasts updates to all the websockets via some protocol you have devised.

All the client will do is instead of sending growls via a form, we'll send the information through the websocket. Here's how you would construct a websocket on the client side. It's all done in javascript.

```javascript
ws = new WebSocket("ws://" + document.domain + ":5000/ws");
```
The protocol on the client side is *event based*. Whereas before, we imperatively call methods on the websockets object, now the websocket kinda hangs around until something happens. The important events are `onmessage` and `onclose`. `onmessage` is triggered when we receive a string from the server, and `onclose` happens when the connection is terminated.

```javascript
ws.onmessage = function(message) {
    //do something
}
ws.onclose = function() {
    //do something
}
```
 We're setting functions that will be called in the future when this events will happen. These functions are called *callbacks*. We don't have to worry about anything else. The websocket library in javascript will trigger the events and call the callbacks for us. All we need to do is specify what happens, and we're done!

 Sending messages is the same as before!

 ```javascript
 ws.send("hello world!");
 ```

We're replacing the form functionality with websockets, which means we need to aggregate the data in the file and send it to the server over the websocket via our protocol.

To get this data, I suggest you use *jQuery*, an amazing javascript plugin that allows you to manipulate HTML like a god. You can download jQuery [here](http://jquery.com/). Add it to your html page with a `<script>` tag but make sure to serve it up on a route in Flask beforehand, just like you did with the static `index.html` before.

If your given html tag has `id='blah'`, you can access the value it has by saying `$("#blah").val()`. This will allow you to grab the data from the existing form elements.

The last important thing you'll need to know is how to get events from the browser, such as a button click or a key press.
Suppose you have a button with `id='send'`. You can set up a callback for the click event by saying:
```javascript
    $("#send").click(function() {
        //do something
    })
```

All right. Those are all the individual pieces needed to make this happen. Now it's up to you to figure out how to join them all together. There's a working solution in this directory for your reference if you ever get stuck.
