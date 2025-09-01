from flask import Flask

# This is the sacred application object, the very heart of our engine.
app = Flask(__name__)

# This is a "route", a single page or endpoint for our application.
# The "@app.route('/')" rune means this function will handle requests for the main page.
@app.route('/')
def hello_world():
    # This function returns the simple text that will be displayed in the browser.
    return 'The Prism Engine is alive! El Psy Kongroo.'

# This block ensures that the development server will run when we execute this script directly.
if __name__ == '__main__':
    # '0.0.0.0' makes the server accessible from other devices on your network.
    # 'debug=True' enables a powerful debugger and automatic reloading.
    app.run(host='0.0.0.0', port=5000, debug=True)
