import os
import tempfile
import pytest
from Main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def read_html(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return content

def get_header_content():
    return read_html("UI/HTML/index.html")

def get_footer_content():
    return read_html("UI/HTML/code-editor.html")

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200

    # بررسی محتوای Header
    assert get_header_content() in response.data

    # بررسی محتوای Footer
    assert get_footer_content() in response.data
