"""
This module contains test regarding rest_api
"""
from nose.tools import eq_, nottest
from mock import patch

from rock_paper_scissors import rest_api


@patch('rock_paper_scissors.rest_api.APP')
@patch('rock_paper_scissors.rest_api.serve')
def test_main_01(serve_mock, app_mock):
    """
    Enter: Simple invoke \
    Exit: The correct framkwork configuration
    """
    # prepare
    real_app_mock = app_mock.app

    # execute
    rest_api.main()

    # verify
    app_mock.add_api.assert_called_once_with('api.yaml')
    serve_mock.assert_called_once_with(real_app_mock, listen='*:8080')


@patch('rock_paper_scissors.rest_api.util')
def test_match_01(util_mock):
    """
    Enter: computer wins \
    Exit: a json that say that computer wins
    """
    generic_testcase_match(util_mock,
                           computer='Scissors',
                           player='Rock',
                           match=2,
                           result='The computer win')

@patch('rock_paper_scissors.rest_api.util')
def test_match_02(util_mock):
    """
    Enter: player wins \
    Exit: a json that say that player wins
    """
    generic_testcase_match(util_mock,
                           computer='Paper',
                           player='Rock',
                           match=1,
                           result='The player win')

@patch('rock_paper_scissors.rest_api.util')
def test_match_03(util_mock):
    """
    Enter: A tie \
    Exit: a json that say that it was a tie
    """
    generic_testcase_match(util_mock,
                           computer='Rock',
                           player='Rock',
                           match=0,
                           result='It is a tie')

@patch('rock_paper_scissors.rest_api.util')
def test_match_04(util_mock):
    """
    Enter: An error on util.match \
    Exit: 'Server Error', 500
    """
    # prepare
    util_mock.match.return_value = 999 # something odd

    # execute
    result = rest_api.match('something')

    eq_(('Server Error', 500), result)


@nottest
def generic_testcase_match(mock, computer='', player='',
                           match=0, result=''):
    """
    Generic function to encampsulate the logic to
    test the match function

    Args:
        mock (MagicMock) mock to configure for the test
        computer (str) Rock, Scissors or Paper
        player (str) Rock, Scissors or Paper
        match (int) Output of the util.match
        result (str) Message that descrbie the winner
    """
    # prepare
    mock.get_computer.return_value = computer
    mock.match.return_value = match
    expected = {
        'player' : player,
        'computer' : computer,
        'resutl_id' : match,
        'result' : result
    }

    # execute
    result = rest_api.match(player)

    # verify
    mock.get_computer.assert_called_once()
    mock.match.assert_called_once_with(player,
                                       computer)
    eq_(expected, result)
