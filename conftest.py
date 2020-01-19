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
