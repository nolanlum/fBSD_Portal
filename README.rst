=====================
fBSD-Community-Portal
=====================
The unofficial FreeBSD Community Portal is being developed as a project
for the Google Code-In event, and will (hopefully) allow simple communication
and collaboration for whatever the FreeBSD organization wishes to use it for.

------------
Dependencies
------------
- `Django Web Framework`_
- django-social-auth_

We use django-social-auth_ to interface with OpenID/OAuth providers.

-----
Setup
-----
Setup of fBSD-Community-Portal is relatively simple.

Verify that all dependencies are installed. The availability of Django can be checked via
a simple python import:

	``>>> import django``

If this completes successfully, Django is installed. Django is available via pipi or easy_install:

	``easy_install django``

Similarly, django-social-auth is installable via the same process. Use pipi or easy_install:

	``easy_install django-social-auth``

Once the dependencies are installed, set up the sqlite database by running:

	``python manage.py syncdb``

This creates the necessary database tables to run this Django project. To start a development server, which
listens by default on ``localhost:8000``, issue the command:

	``python manage.py runserver``

All the 3rd party authentication services are configured to accept ``http://localhost:8000`` as a redirect URL.
Configuration for a live site with a different domain name will require reconfiguration of the authentication providers which
require app registration (at this time only Facebook and LinkedIn.)

.. _Django Web Framework: https://www.djangoproject.com/
.. _django-social-auth: https://github.com/omab/django-social-auth