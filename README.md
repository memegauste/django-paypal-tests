![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
# django-paypal-tests
Test PayPal cyclic payments with simple Django app.

Requires Python 3.12 or newer and Django 6.1.2. The default development
version is Python 3.15.0; CI runs lint, Django checks, migration checks,
and tests on Python 3.12, 3.13, 3.14, and 3.15.

### Development

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements_dev.txt
python manage.py migrate
python manage.py runserver
```

SQLite is used by default. For local deployment settings, copy
`project/settings_local.example` to `project/settings_local.py` and adjust
the database credentials and allowed hosts.

### Checks and tests

```sh
python -m pip check
python -m flake8 .
python manage.py check
python manage.py makemigrations --check --dry-run
python -m pytest --cov=project --cov=testapp --cov-report=term-missing
```

Coverage is reported locally and in CI with pytest-cov. The unused legacy
Codecov and Coveralls upload clients have been removed.

### Why you might need it?
* Because you need to test response from second, third... cyclic paypal payments
* You want to see how to implement subscription under Django

REMEMBER! Set the CORRECT IPN server to your deployed app in account paypal settings.
