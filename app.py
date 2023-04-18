from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)

health = HealthCheck()

@app.route('/')
def hello_world():
  return 'Hello, Docker!'

def app_available():
  return True, "app ok"

health.add_check(app_available)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
