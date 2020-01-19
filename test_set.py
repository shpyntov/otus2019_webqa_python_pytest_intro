import pytest


def test_set_clear(random_set):
    random_set.clear()
    assert len(random_set) == 0


@pytest.mark.parametrize("new_element", [-1, 0, 10, 999, 'asd'])
def test_set_add(random_set, new_element):
    random_set.add(new_element)
    assert new_element in random_set


@pytest.mark.parametrize("new_element", [-1, 0, 10, 999, 'asd'])
def test_set_remove(random_set, new_element):
    random_set.add(new_element)
    assert new_element in random_set
    random_set.remove(new_element)
    assert new_element not in random_set


def test_set_update():
    set1 = {1, 2, 3}
    set2 = {4.01, 5, "six"}
    set1.update(set2)
    assert set1 == {1, 2, 3, 4.01, 5, "six"}
