import pytest

import source.shapes as shapes

@pytest.fixture
def get_rectangle():
    return shapes.Rectangle(4,5) ## get object

@pytest.fixture
def get_other_rectangle():
    return shapes.Rectangle(5, 4)  ## get object