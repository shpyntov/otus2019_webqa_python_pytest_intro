import pytest


def test_string_lower(random_string):
    assert random_string.lower() == ' test string '


def test_string_split(random_string):
    assert random_string.split() == ['Test', 'String']


def test_string_strip(random_string):
    assert random_string.strip() == 'Test String'


@pytest.mark.parametrize("words", [['Test', 1], ['String', 6], ['Number', -1]])
def test_list_find(random_string, words):
    assert random_string.find(words[0]) == words[1]
