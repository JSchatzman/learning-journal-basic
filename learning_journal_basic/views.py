from pyramid.response import Response
import os


THIS_DIR = os.path.dirname(__file__)


def home(request):
    """Home view handler."""
    file_contents = open(os.path.join(THIS_DIR, 'templates/index.jinja2')).read()
    return Response(file_contents)


def detail(request):
    """Detail view handler."""
    file_contents = open(os.path.join(THIS_DIR, 'data/journal.html')).read()
    return Response(file_contents)


def create(request):
    """Create new view handler."""
    file_contents = open(os.path.join(THIS_DIR, 'templates/new_entry.html')).read()
    return Response(file_contents)


def update(request):
    """Update/edit view handler."""
    file_contents = open(os.path.join(THIS_DIR, 'templates/edit_entry.html')).read()
    return Response(file_contents)


def includeme(config):
    """Pyramid view configuration."""
    config.add_view(home, route_name="home")
    config.add_view(detail, route_name="detail")
    config.add_view(update, route_name="update")
    config.add_view(create, route_name="create")