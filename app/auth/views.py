from flask import render_template, request, redirect, url_for, abort
from . import auth

# Views


@auth.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title=title)
