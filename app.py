import random
import time
import names
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

name_list = [names.get_first_name() for i in range(10)]


def get_hit_count(name):
    retries = 5
    while True:
        try:
            return cache.hincrby('hits', name, 1)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    name = random.choice(name_list)
    count = get_hit_count(name)
    return '<h1><span style="color: blue;">Hello {}!</span><br> ' \
           'You have visited <span style="color: red;">{} times.</span></h1>'.format(name, count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
