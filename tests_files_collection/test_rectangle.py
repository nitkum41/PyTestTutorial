import pytest

import source.shapes as shapes



def test_area(get_rectangle):

    assert get_rectangle.area() == 4*5

def test_perimeter(get_rectangle):

    assert get_rectangle.perimeter() == 2*(9)

#fixtures from conftest.py file accessible
def test_different_rectangles(get_rectangle,get_other_rectangle):
    assert get_rectangle != get_other_rectangle