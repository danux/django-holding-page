# Django Holding Page

An out-the-box viral holding page for your websites with export functionality. This project started as a solution to basic
problem of what to put on new domain names while development was occurring.

[![Build Status](https://travis-ci.org/danux/django-holding-page.svg?branch=master)](https://travis-ci.org/danux/django-holding-page)

Tested on:

- Python 2.7.9
- Python 3.2
- Python 3.3
- Python 3.4
- Python 3.5

## Features

- Users can provide their email address and name which is saved in to the database for future exports to systems such as Campaign Monitor.
- Each user is sent a viral code, which allows them to share your holding page with other people and build up points.
- Complete use of templates - configure the entire app to your own needs without touching the code

## Usage

Usage guidelines will be added once the setup.py stuff is setup.

## Development

    git clone git://github.com/danux/django-holding-page.git
    cd django-holding-page
    pip install -r requirements.txt
    ./manage.py test
    ./manage.py migrate

Restyle subscriber/templates/subscriber/*.html
Reword subscriber/templates/email/welcome_*.txt to suit your project

## Development Roadmap/Ideas

- Add a setup.py and other jazz to get this in to pypi
- Add support for Travis
- Auto-export to Campaign Monitor, Sales Force, etc
- "Reserve my username" feature
- Make it easy to integrate this as a beta holding pen for Django projects (i.e. issue beta invites to your subscribers)
- Will i18n it at some point (though it really wouldn't be hard to do yourself)
- Anything else you fancy adding/suggesting
- Pull requests will be reviewed if you choose to share back.
