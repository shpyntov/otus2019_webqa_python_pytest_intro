import pytest
import random
import copy


@pytest.fixture
def lst():
    return random.sample(range(30), 4)

@pytest.fixture
def element():
    return random.randint(-100, 100)


def test_list_clearing(lst):
    lst.clear()
    assert len(lst) == 0


def test_list_append(lst, element):
    lst.append(element)
    assert lst[-1] == element


def test_list_reverse(lst):
    orig_lst = copy.deepcopy(lst)
    lst.reverse()
    assert lst == orig_lst[::-1]

def test_list_insert(lst, element):
    lst.insert(2, element)
    assert lst[2] == element