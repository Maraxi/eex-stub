# Development

## Setup
Make sure to have `python3` and `pipenv` installed.

Install virtual python environment with all needed packages for development with:
`pipenv shell`

Inside this environment install the pre-commit hooks with:
`pre-commit install`
With every commit python code style will now be enforced.
The commit hooks may be skipped by running:
`git commit --no-verify`

Django sets up a server which runs all code and handles all Object management, error logging and email sending.
The database needs to migrate to the latest state first.
`python ecc/manage.py migrate`

An interactive server may be run with `python ecc/manage.py runserver`. However admin access or visible frontend views are not yet implemented.

Tests may be run with `python ecc/manage.py test margin_reports`.

Django offers an interactive shell with `python ecc/manage.py shell` that allows testing of all functionality. Database entries may be created here and logs can be accessed.
