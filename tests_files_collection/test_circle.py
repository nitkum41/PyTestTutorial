import math

import pytest

import source.shapes as shapes

class TestCircle:

    def setup_method(self,method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(10) #circle object

    def teardown_method(self,method):
        print(f"teardown down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter()==2*math.pi*self.circle.radius