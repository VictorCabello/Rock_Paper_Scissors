"""
Module to test the utils module
"""
from mock import patch, call

from rock_paper_scissors import util


def test_verify_01():
    """
    Input: 'Rock'
    Exepcted: True
    """
    pass


@patch('rock_paper_scissors.util.verify')
def test_match_01(verify_mock):
    """
    test_match use verify correctly
    Expected: 2 inovkations to verify
    """
    util.match('Scissors', 'Paper')

    expected_calls = [call('Scissors'),
                      call('Paper')]
    verify_mock.assert_has_calls(expected_calls)


def test_get_computer_01():
    """
    Input: None \
    Expected: a number from the mock
    """
    pass
