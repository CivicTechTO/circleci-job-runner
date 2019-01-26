from flask import Flask, request
import os
import requests


CIRCLE_API_USER_TOKEN = os.environ.get('CIRCLE_API_USER_TOKEN')
BRANCH = os.environ.get('GIT_BRANCH')
REPO = os.environ.get('GITHUB_REPO')

app = Flask(__name__)

@app.route('/')
def home():
    return('Hello World!')

@app.route('/jobs/<job_name>', methods=['POST'])
def do_job_action(job_name=None):
    if request.method == 'POST':
        return run_job(job_name)
    else:
        return 'Not found', 404

def get_default_branch():
    r = requests.get('https://api.github.com/repos/' + REPO)
    return r.json()['default_branch']

def run_job(job_name=None):
    payload = {
        'build_parameters': {
            'CIRCLE_JOB': job_name,
        },
    }
    branch = get_default_branch() if not BRANCH else BRANCH
    endpoint = 'https://circleci.com/api/v1.1/project/github/{}/tree/{}'.format(REPO, branch)
    r = requests.post(endpoint,
                      auth=(CIRCLE_API_USER_TOKEN, ''),
                      json=payload)

    return r.text
