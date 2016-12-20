from pyramid.response import Response
import io
import os
from pyramid.view import view_config
# THIS_DIR = os.path.dirname(__file__)
"""

def home_page(request):
    imported_text = io.open('/templates/index.html').read()
    return Response(imported_text)

def new_entry(request):
    imported_text = io.open('/templates/new_entry.html').read()
    return Response(imported_text)

def edit_entry(request):
    imported_text = io.open('/templates/edit_entry.html').read()
    return Response(imported_text)

def journal_entry(request):
    imported_text = io.open('/templates/journal_entry.html').read()
    return Response(imported_text)

"""

"""
@view_config(route_name='home', renderer='templates')
def my_view(request):
    #return {'project': 'learning_journal_basic'}
    return 

"""
@view_config(route_name='home', renderer='/templates/index.jinja2')
def home_page(request):
    #return Response(imported_text)
    return {'test': 'testvalue'}



def includeme(config):
    config.add_view(home_page,
                    route_name='home'
                    )

"""from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'learning_journal_basic'}
"""