from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

def read_html(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return content

@app.get("/", response_class=HTMLResponse)
def read_main_html():

    """
    Read and return the content of the main HTML file.

    Returns:
    HTMLResponse: The HTML content.
    """
    my_file = read_html("UI/HTML/index.html")
    return my_file

@app.get("/Code/", response_class=HTMLResponse)
def read_code_editor_html():

    """
    Read and return the content of the code editor HTML file.

    Returns:
    HTMLResponse: The HTML content.
    """

    my_file = read_html("UI/HTML/code-editor.html")
    return my_file

@app.exception_handler(404)
async def page_not_found(request, exc):

    """
    Handle 404 errors by returning a custom HTML page.

    Returns:
    HTMLResponse: The HTML content for the 404 page.
    """
    
    my_file = read_html("UI/HTML/404.html")
    return HTMLResponse(content=my_file, status_code=404)

if __name__ == '__main__':
    os.system("clear")
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
