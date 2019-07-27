"""Request information.

HTTP communication starts with an HTTP Request. It's a request from a client
to access a particular resource.
Flask wraps the request info in a `request` object which can be used
in any view or template (automatically available).

Docs: http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/request-info')
def request_info():
    ip_url = 'http://ip-api.com/json/{}'.format(request.remote_addr)
    client_location = requests.get(ip_url).json()
    return render_template('request/info.html',
                           client_location=client_location)
