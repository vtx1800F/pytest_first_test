import pytest
from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc= Calculator

    def test_miltiplay_calculate_correctly(self):
        assert self.calc.multiply(self, 2 ,2)==4

    def test_divisiom(self):
        assert self.calc.division(self, 6 ,2)==3

    def test_subtraction(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding(self):
        assert self.calc.adding(self, 3, 4) == 7

