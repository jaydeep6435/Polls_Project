-----
Polls
-----

Polls is a Django web app to conduct web-based polls. For each question, a voter can choose from one of the many number of answers.

Quick start
-----------

1. Add "polls" to your project by configuring INSTALLED_APPS setting like this::

INSTALLED_APPS - [
        ...
        'polls',
]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
