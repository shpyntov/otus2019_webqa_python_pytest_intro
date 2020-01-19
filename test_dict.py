# тестирование методов работы со словарями

import pytest


def test_dict_clear(random_dict):
    random_dict.clear()
    assert len(random_dict) == 0


@pytest.mark.parametrize("test_data", [[0, 0], [3, 9], [5, 25]])
def test_dict_get(random_dict, test_data):
    assert random_dict.get(test_data[0]) == test_data[1]


def test_dict_values(random_dict):
    assert list(random_dict.values()) == [0, 1, 4, 9, 16, 25, 36]


def test_dict_keys(random_dict):
    assert list(random_dict.keys()) == [0, 1, 2, 3, 4, 5, 6]
