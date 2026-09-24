import os
from datetime import datetime, timezone

from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        application="sample-time-app",
        message="Visit /time to get the current time.",
    )


@app.get("/time")
def current_time():
    now = datetime.now(timezone.utc)
    return jsonify(
        current_time=now.isoformat().replace("+00:00", "Z"),
        timezone="UTC",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8080")),
        debug=False,
    )
