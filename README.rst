**********
Powermeter
**********

Project to apply to Powermeter position.

Installing with Docker
======================

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

      $ sudo docker run -it -p 8020:8020 powermeter

The site will be available on <http://0.0.0.0:8020>.

Installing manually
===================

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
