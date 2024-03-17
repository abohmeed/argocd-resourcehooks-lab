import os
from flask import Flask
from redis import Redis, RedisError

# Retrieve Redis password from environment variable
redis_password = os.environ.get('REDIS_PASSWORD')
redis_host = os.environ.get('REDIS_HOST')

# Connect to Redis with authentication
redis = Redis(host=redis_host, port=6379, db=0, decode_responses=True, password=redis_password)

app = Flask(__name__)

@app.route('/')
def hello():
    visits = redis.incr('counter')  # Increment the counter in Redis
    html = "<h3>Hello from Flask!</h3>" \
           "<b>Visits:</b> {visits}"
    return html.format(visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

