# тестирование методов работы со списками

import pytest
import copy


def test_list_clear(random_list):
    random_list.clear()
    assert len(random_list) == 0


def test_list_append(random_list, random_int):
    random_list.append(random_int)
    assert random_list[-1] == random_int


def test_list_reverse(random_list):
    orig_lst = copy.deepcopy(random_list)
    random_list.reverse()
    assert random_list == orig_lst[::-1]


@pytest.mark.parametrize("pos", [1, 2, 3, 4, 5])
def test_list_insert(random_list, random_int, pos):
    random_list.insert(pos, random_int)
    assert random_list[pos] == random_int
