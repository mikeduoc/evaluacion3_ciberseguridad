from flask import Flask, request, make_response
from markupsafe import escape
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.after_request
def security_headers(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.route("/")
def index():
    user_input = request.args.get("input", "")
    safe_input = escape(user_input)
    response = make_response(f"<h1>{safe_input}</h1>")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)