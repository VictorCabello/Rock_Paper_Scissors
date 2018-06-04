"""
This module define all the steps used on the stories for BDD
"""
from lettuce import step, world, before
import sure

from rock_paper_scissors.rest_api import APP


@before.all
def before_all():
    """
    Prepare test server
    """
    print sure.version
    APP.add_api('api.yaml')
    world.app = APP.app.test_client()


@step(u'I send "([^"]*)" as player to the "/match" service')
def send_player(_, player_chooise):
    """
    Send any string as player value to the match service
    """
    world.response = \
        world.app.get('/match#?player={}'.format(player_chooise))


@step(u"I don't send player as match service's parameter")
def send_player_none(_):
    """
    Send any string as player value to the match service
    """
    world.response = world.app.get('/match')


@step(u'I see a response with title "([^"]*)" and status "([^"]*)"')
def reponse_send_player(_, title, status_code):
    response = world.response
    assert (response.get_json()['title']).should.eql(title)
    assert (response.status_code).should.eql(int(status_code))
