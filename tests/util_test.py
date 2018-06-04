"""
Module to test the utils module
"""
from nose.tools import ok_, raises, eq_
from mock import patch, call

from rock_paper_scissors import util


def test_verify_01():
    """
    Input: 'Rock'
    Exepcted: True
    """
    result = util.verify('Rock')
    ok_(result)

def test_verify_02():
    """
    Input: 'Paper'
    Exepcted: True
    """
    result = util.verify('Paper')
    ok_(result)

def test_verify_03():
    """
    Input: 'Scissors'
    Exepcted: True
    """
    result = util.verify('Scissors')
    ok_(result)

@raises(ValueError)
def test_verify_04():
    """
    Input: invalid value
    Expected: ValueError
    """
    util.verify('somethingelse')


@patch('rock_paper_scissors.util.verify')
def test_match_01(util_mock):
    """
    test_match use verify correctly
    Expected: 2 inovkations to verify
    """
    util.match('Scissors', 'Paper')

    expected_calls = [call('Scissors'),
                      call('Paper')]
    util_mock.assert_has_calls(expected_calls)

@patch('rock_paper_scissors.util.verify')
def test_match_02(util_mock):
    """
    Input: p1=Scissors p2=Paper \
    Expected: 1
    """
    result = util.match('Scissors', 'Paper')

    util_mock.assert_called()
    ok_(result == 1, 'The result was ' + str(result))

@patch('rock_paper_scissors.util.verify')
def test_match_03(util_mock):
    """
    Input: p1=Rock p2=Scissors \
    Expected: 1
    """
    result = util.match('Rock', 'Scissors')

    util_mock.assert_called()
    ok_(result == 1, 'The result was ' + str(result))

@patch('rock_paper_scissors.util.verify')
def test_match_04(util_mock):
    """
    Input: p1=Paper p2=Rock \
    Expected: 1
    """
    result = util.match('Paper', 'Rock')

    util_mock.assert_called()
    ok_(result == 1, 'The result was ' + str(result))


@patch('rock_paper_scissors.util.randint')
def test_get_computer_01(randint_mock):
    """
    Input: None \
    Expected: a number from the mock
    """
    random_number = 1
    randint_mock.return_value = random_number
    result = util.get_computer()

    randint_mock.assert_called_once_with(0, 2)
    eq_(result, util.OPTIONS[random_number])
