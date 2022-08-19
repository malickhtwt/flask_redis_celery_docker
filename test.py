import pytest
from flask import Flask, url_for
from redis import Redis

class TestPage(object):
	def test_one(self):
		x = "This"
		assert "h" in x

	def test_two(self):
		x = "hello"
		assert hasattr(x,"check")

	def test_universities(self):
		app = Flask(__name__)
		client = app.test_client()
		ctx = app.app_context()
		ctx.push()
		url = '/universities'
		response = client.get(url)
		assert response.status_code == 404

	def test_redis(self):
		redis = Redis(host='redis', port='6379')
		#redis.set('mykey', 'hello from python')
		value = redis.get('mykey')
		assert value == b'hello from python'