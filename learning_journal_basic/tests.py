# tests.py
import pytest
from pyramid import testing


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    """Test that the contents of the root page contain expected text."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Learning Blog' in html.find("h1").text


def test_root_contents(testapp):
    """Test that the contents of the root page contains all journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    """ There should be one link that is not a link to specific article."""
    assert len(ENTRIES) == len(html.findAll("a")) - 1


def test_update_page_renders_file_data(testapp):
    """Ensure my update  some data."""
    from .views import ENTRIES
    response = testapp.get('/journal/0', status=200)
    assert 'lecture was difficult' in str(response.html)


def test_edit_entry_page_exists(testapp):
    """Test that multiple journal pages exist."""
    response = testapp.get("/journal/0/edit-entry", status=200)
    html = response.html
    assert 'submit' in str(response.html)
