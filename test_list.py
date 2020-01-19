import pytest
import copy


def test_list_clearing(rndm_list):
    rndm_list.clear()
    assert len(rndm_list) == 0


def test_list_append(rndm_list, rndm_int):
    rndm_list.append(rndm_int)
    assert rndm_list[-1] == rndm_int


def test_list_reverse(rndm_list):
    orig_lst = copy.deepcopy(rndm_list)
    rndm_list.reverse()
    assert rndm_list == orig_lst[::-1]


@pytest.mark.parametrize("pos", [1, 2, 3, 4, 5])
def test_list_insert(rndm_list, rndm_int, pos):
    rndm_list.insert(pos, rndm_int)
    assert rndm_list[pos] == rndm_int
