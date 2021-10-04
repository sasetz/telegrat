import core
from bottle import run
from subscription import updates
import config

if __name__ == '__main__':
    core.start()
    run(host="0.0.0.0", port=config.port)
