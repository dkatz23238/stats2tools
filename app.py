from flask import Flask
from stat2tools.exponential import exponential
from stat2tools.gamma import gamma_f
from stat2tools.normal import gaussian

from flask import request, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/exponential")
def get_exponential():
    l = float(request.args.get("lambda", 0.1))
    sample_size = int(request.args.get("sample_size", 55))
    n_samples = int(request.args.get("n_samples", 100))
    r = exponential(l, sample_size, n_samples)
    print(l)
    return jsonify(r)


@app.route("/gamma")
def get_gamma():
    alpha = float(request.args.get("alpha", 2))
    theta = float(request.args.get("theta", 3))
    sample_size = int(request.args.get("sample_size", 55))
    n_samples = int(request.args.get("n_samples", 100))
    r = gamma_f(alpha, theta, sample_size, n_samples)
    return jsonify(r)


@app.route("/normal")
def get_normal():
    mu = float(request.args.get("mu", 100))
    sigma = float(request.args.get("sigma", 20))
    sample_size = int(request.args.get("sample_size", 55))
    n_samples = int(request.args.get("n_samples", 100))
    r = gaussian(mu, sigma, sample_size, n_samples)
    return jsonify(r)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

