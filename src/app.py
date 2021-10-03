import core
from bottle import run
import os


if __name__ == '__main__':
    core.start()
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
