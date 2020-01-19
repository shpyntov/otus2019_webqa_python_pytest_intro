import pytest
import random
import string


@pytest.fixture
def random_list():
    return random.sample(range(100), 5)


@pytest.fixture
def random_set():
    return set(random.sample(range(100), 5))


@pytest.fixture
def random_int():
    return random.randint(-100, 100)


@pytest.fixture
def random_string():
    return ' Test String '


@pytest.fixture
def random_dict():
    return {a: a ** 2 for a in range(7)}
#   return {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
