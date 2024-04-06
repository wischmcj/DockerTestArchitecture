import time

import redis
import debugpy
from flask import Flask, render_template, abort

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379)

def pre_populate_cache():
    cache.hset('post', 1, 'First Content')
    return
    

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
            
def set_post(post_id, post_text):
    post = cache.hset('post',post_id, post_text)
    return post

def get_post(post_id):
    post = cache.hget('post', 'First')
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/hello')
def hello():
    count = get_hit_count()
    return 'Hello World! I have now been seen {} times.\n'.format(count)

@app.route('/')
def index():
    cache.hset('post', 'First', 'First Content')
    posts = get_post('post')
    return  render_template('index.html',posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')


if __name__ == '__main__':
    # pre_populate_cache()
    app.run(debug=True, host='0.0.0.0')