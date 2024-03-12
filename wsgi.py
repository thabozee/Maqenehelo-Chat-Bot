import site

activate_this = '/var/www/html/python-applications/loyalty_api/venv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(_file_=activate_this))

import sys

sys.path.insert(0, "/var/www/html/python-applications/loyalty_api")

site.addsitedir("/var/www/html/python-applications/loyalty_api/venv/lib64/python3.6/site-packages/")

from src.view.app import build

application = build()
