import requests
from flask import Flask, jsonify, request
from flask_caching import Cache  # Import Cache from flask_caching module
from redis import Redis
from flask_celery import make_celery

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Set the configuration variables to the flask application
cache = Cache(app)  # Initialize Cache
celery = make_celery(app)

#flask caching example using redis
@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

#use redis as a DB example
@app.route('/data')
def connect_to_redis():
    redis = Redis(host='redis', port='6379')
    redis.set('mykey', 'hello from python')
    value = redis.get('mykey')
    return value

#celery example for running task in the background with redis
@app.route('/celery')
def call_add_together():
    result = add_together.delay(23,42)
    result.wait()
    return 'I sent an async request'

@celery.task(name='add_together')
def add_together(a,b):
    return a+b

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
