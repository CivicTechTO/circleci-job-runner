# CircleCI Job Runner

Simple API for running CircleCI jobs via public endpoints.

The purpose of this app is to allow "safe" CircleCI jobs to be run
on-demand without credentials. This is intended to allow organizational
house-keeping tasks captured in scripts to be run by [chatbot
commands]() and through [custom menus in Google Docs]().

## Use-Cases

This section is a work-in-progress.

## Usage

Configure the app appropriately, and POST to endpoints of the following
format:

`https://myapp.herokuapp.com/jobs/my_job_name`

The specific job name will depend how you've named them in your target
repo's `.circleci/config.yml`.

## Configuration

- `GITHUB_REPO`. The repo from which the jobs should be run. Example:
  `CivicTechTO/civictechto-scripts`.

- `GIT_BRANCH`. The name of the branch from which the code should be
  run. This defaults to the default branch as [set through
GitHub](https://help.github.com/articles/setting-the-default-branch/).
(Optional)

- `CIRCLE_API_USER_TOKEN`. A [personal API token][personal-token] for a
  user with appropriate permissions on the repo. Having write access on
the GitHub repo should give proper access. (Project tokens are
read-only, and so won't work.)

   [personal-token]: https://circleci.com/docs/2.0/managing-api-tokens/#creating-a-personal-api-token

## Local Development

```
cp sample.env .env
# Customize values in .env
pipenv install
pipenv run flask run
```

## Related Projects

- [`hubot-toby`](https://github.com/civictechto/hubot-toby)
- [`civictechto-scripts`](https://github.com/civictechto/civictechto-scripts)

## To Do

- [ ] Create landing page.
- [ ] Add redirects to landing page.
- [ ] Create swagger doc and link on landing page.
- [x] Use default branch.
- [ ] Add heroku deploy button.
- [ ] Add whitelist/blacklist for job names.
- [ ] Add tests.
- [ ] Add auto-deploy to Heroku.
- [ ] Add ability to set repo/branch in POST data.
- [ ] Convert to a GitHub app.
