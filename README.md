# CircleCI Job Runner

Simple API for running CircleCI jobs via public endpoints.

The purpose of this app is to allow "safe" CircleCI jobs to be run
on-demand without credentials. This is intended to allow organizational
house-keeping tasks captured in scripts to be run by [chatbot
commands]() and through [custom menus in Google Docs]().

## Usage

Configure the app appropriately, and POST to endpoints of the following
format:

`https://myapp.herokuapp.com/jobs/my_job_name`

The specific job name will depend how you've named them in your target
repo's `.circleci/config.yml`.

## Configuration

- `CIRCLE_API_USER_TOKEN`

- `GITHUB_REPO`. Example: `CivicTechTO/civictechto-scripts`.

- `GIT_BRANCH`. The name of the branch on GitHub to run the job against.

## Related Projects

- `hubot-toby`
- `civictechto-scripts`
