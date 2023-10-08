import os
from flask import Flask, render_template

app = Flask(__name__)

def read_html(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return content

@app.route('/')
def hello_world():

    """
    Endpoint to display the content of the main HTML file.

    Returns:
    str: The HTML content.
    """
    my_file = read_html("UI/HTML/index.html")
    return my_file

@app.route('/Code/')
def start():

    """
    Endpoint to display the content of the code editor HTML file.

    Returns:
    str: The HTML content.
    """

    my_file = read_html("UI/HTML/code-editor.html")
    return my_file

@app.errorhandler(404)
def page_not_found(error):

    """
    Error handler for 404 errors, displays a custom 404 page.

    Returns:
    tuple: A tuple containing the HTML content and the HTTP status code (404).
    """
    
    my_file = read_html("UI/HTML/404.html")
    return render_template(my_file), 404

if __name__ == '__main__':
    os.system("clear") and os.system("cls")
    app.run()
