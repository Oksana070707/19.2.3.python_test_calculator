import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtruction_calculate_correctly(self):
        assert self.calc.subtruction(self, 6, 5) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 7, 3) == 10




