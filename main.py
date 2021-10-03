from core import *
from bottle import run
import os

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host=setup.base_url, port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
