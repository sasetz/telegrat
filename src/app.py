from core import *
from bottle import run
import os


if __name__ == '__main__':
    run(host=setup.base_url, port=int(os.environ.get("PORT", 5000)))
