import os
from pyramid.view import view_config


ENTRIES = [

    {
        "id": 2,
        "title": "Literally NoSQL",
        "body": "Today I came to the realization of how learning in this class will work for me, and likely most of the class. When Pyramid was introduced I did not understand what was going on. One day after the introduction, the first assignment sounds like a breeze. It seems things start to soak in the next day instead of during lecture. The human brain acts in funny ways. I've also come to accept the fact that this class will take over my life until it is over. it's a significant sacrifice that people more knowledgeable than myself think I must take to get to where I know I want to go.",
        "date": "Dec. 21, 2016"
    },


    {
        "id": 1,
        "title": "Jinja Ninja",
        "body": "After reading some of posts by other people, I feel like the only person in the whole class who's having a harder time with the frameworks than with the echo server assignment.  The fact that I did not take the 301 class is really showing which is unfortunate but I think I can catch up in due time.",
        "date": "Dec. 20, 2016"
    },


    {
        "id": 0,
        "title": "Introduction to Pyramid",
        "body": "Today's lecture was difficult for me to follow due to the breakneck speed. I enjoyed working on the deque today, it was a breeze and I'm really seeing the value of class composition. Once I got to working on the pyramid assignment I was pretty lost and I'm still trying to work through it. I have no doubt that pyramid is awesome, and while I can follow along with the class notes, I'm not really at a point yet where I understand what's going on. I'm hoping that will change soon.",
        "date": "Dec. 19, 2016"
    },
]


THIS_DIR = os.path.dirname(__file__)


@view_config(route_name='home', renderer='templates/index2.jinja2')
def home_view(request):
    """Home view handler."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='data/journal.jinja2')
def detail_view(request):
    """Detail view handler."""
    entry_id = int(request.matchdict['id'])
    return {'entry': ENTRIES[entry_id]}


@view_config(route_name='create', renderer='templates/new_entry.jinja2')
def create_view(request):
    """Create new view handler."""
    return {'name': 'Home View'}


@view_config(route_name='update', renderer='templates/edit_entry.jinja2')
def update_view(request):
    """Update/edit view handler."""
    return {'name': 'Home View'}
