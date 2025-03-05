import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length,expected_area",[(4,16),(5,25)])
def test_multiple_square_area(side_length,expected_area):
    assert shapes.Square(side_length).area()==expected_area


@pytest.mark.parametrize("side_length,expected_perimeter",[(4,16),(5,20)])
def test_multiple_square_perimeter(side_length,expected_perimeter):
    assert shapes.Square(side_length).perimeter()==expected_perimeter