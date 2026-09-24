from datetime import datetime, timezone

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def current_time():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
