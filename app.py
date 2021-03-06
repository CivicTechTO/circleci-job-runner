from flask import Flask, request
import json
import os
import requests
import yaml


CIRCLE_API_TOKEN = os.environ.get('CIRCLE_API_USER_TOKEN', '')
BRANCH = os.environ.get('GIT_BRANCH', '')
REPO = os.environ.get('GITHUB_REPO', '')
JOBS_BLACKLIST = os.environ.get('JOBS_BLACKLIST', 'default').split(',')

app = Flask(__name__)

if not REPO or not CIRCLE_API_TOKEN:
    raise 'Environment variables not set for GitHub repo and/or CircleCI API token. Exiting...'

@app.route('/')
def home():
    return('Hello World!')

@app.route('/jobs', methods=['GET'])
def list_jobs():
    if request.method == 'GET':
        return get_job_names()
    else:
        return 'Not found', 404

@app.route('/jobs/<job_name>', methods=['POST'])
def do_job_action(job_name=None):
    if request.method == 'POST':
        return run_job(job_name)
    else:
        return 'Not found', 404

def get_default_branch():
    r = requests.get('https://api.github.com/repos/' + REPO)
    return r.json()['default_branch']

def get_job_names():
    branch = get_default_branch() if not BRANCH else BRANCH
    config_url = 'https://raw.githubusercontent.com/{}/{}/.circleci/config.yml'.format(REPO, branch)
    r = requests.get(config_url)
    config = yaml.safe_load(r.text)
    job_names = list(config['jobs'].keys())
    job_names = [j for j in job_names if j not in JOBS_BLACKLIST]
    return json.dumps(job_names)

def run_job(job_name=None):
    payload = {
        'build_parameters': {
            'CIRCLE_JOB': job_name,
        },
    }
    branch = get_default_branch() if not BRANCH else BRANCH
    endpoint = 'https://circleci.com/api/v1.1/project/github/{}/tree/{}'.format(REPO, branch)
    r = requests.post(endpoint,
                      auth=(CIRCLE_API_TOKEN, ''),
                      json=payload)

    return r.text
