import pytest
from src.triangle import triangle_type


def test_equilatero():
        assert triangle_type(8,8,8) == "Equilateral"

def test_escaleno():
        assert triangle_type(20,18,24) == "Scalene"

def test_isosceles(): 
        assert triangle_type(20,20,24) == "Isosceles"


def test_invalid():
        assert triangle_type(5,9,15) == "Not a triangle"

