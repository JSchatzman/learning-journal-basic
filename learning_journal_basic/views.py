from pyramid.response import Response
import io
import os

THIS_DIR = os.path.dirname(__file__)

def home_page(request):
    imported_text = open(os.path.join(THIS_DIR, 'sample.txt')).read()
    file_date = io.open('data/sample.txt').read()
    return Response(imported_text)

def includeme(config):
    config.add_view(home_page,
                    route_name='home'
                    )

"""from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'learning_journal_basic'}
"""