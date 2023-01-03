**********
Powermeter
**********

Project to apply to Powermeter position.

Getting started
===============

Prerequisites
-------------

* Python >= 3.10.6

Installing
----------

1. Create the virtual environment. I recommend using
   `virtualenvwrapper <http://virtualenvwrapper.readthedocs.io/en/latest/index.html>`_.

2. Setup the environment:

   .. code-block:: bash

      $ pip install -r requirements.txt
      $ python manage.py migrate

3. Start the server:

   .. code-block:: bash

      $ python manage.py runserver

The site will be available on <http://localhost:8000> or <http://127.0.0.1:8000>.

REST API
========

REST API documentation will be available on <http://localhost:8000/api/docs/>.

Requirements
============

We use constraints.

Add dependencies to requirements.txt:

   .. code-block:: text

      # requirements.txt
      -c constraints.txt
      Django
      anotherdependency

Then run:

   .. code-block:: bash

      $ pip install -r requirements.txt
      $ pip freeze > constraints.txt
