from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/dispatch_github')
def dispatch_github():
    token = request.args.get('token')
    user = request.args.get('user')
    repo = request.args.get('repo')
    event_type = request.args.get('event_type')
    requests_path = 'https://api.github.com/repos/' + user + '/' + repo + '/dispatches'
    token = 'token ' + token
    r = requests.post(requests_path,
                      json={"event_type": event_type},
                      headers={
                          'Content-Type': 'application/json',
                          'Accept': 'Accept: application/vnd.github+json',
                          'Authorization': token}
                      )
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)
