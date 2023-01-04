**********
Powermeter
**********

Project to apply to Powermeter position.

The site is hosted on `http://44.203.53.169 <http://44.203.53.169/api/docs/>`_.

Getting started
===============

Prerequisites
-------------

* Python >= 3.8

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

Deploy
======

TODO:

* Use environment variables for settings, ideally with `django-environ <https://django-environ.readthedocs.io/en/latest/>`_.
* Use volumes for sqlite database.

Prerequisites
-------------

* Docker >= 20.10.22

Installing
----------

1. Build the image:

   .. code-block:: bash

      $ sudo docker build . -t powermeter

2. Run the container:

   .. code-block:: bash

      $ sudo docker run -d -it -p 80:8020 powermeter

REST API
========

REST API documentation will be available on `/api/docs/`.

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
