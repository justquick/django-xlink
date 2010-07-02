Django Cross Link Documentation
===============================

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1

::

    pip install django-xlink==0.1.1

Django Cross Link takes in particular URLs on an external site and periodically
combs through those URLs searching for links back to your site. The cross
site links are stored in the database for future use and display

Requirements
--------------

XLink requires `lxml <http://codespeak.net/lxml/>`_ for HTML parsing::

    pip install lxml
    
Setup
------

Add ``xlink`` to your ``INSTALLED_APPS`` and run ``./manage.py syncdb``

Add some queries in the admin so xlink knows which URLs to comb through and which
domain (usually your own site's) you want to search for cross linking.

Next run the management command ``./manage.py xlink_search`` which will take the queries
and populate them with results of cross site links.

I recomend putting the management command in a cronjob every hour or so to make
the results appear in real time.


TODO
-----

Spider pages starting at one URL looking for cross site links