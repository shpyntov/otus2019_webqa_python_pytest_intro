import pytest
import random


@pytest.fixture
def rndm_list():
    return random.sample(range(100), 5)


@pytest.fixture
def rndm_int():
    return random.randint(-100, 100)