
import pytest
from pytest import approx

from examples.math_operations import math_operations

def test_add_operations():
    result=math_operations(1,3)
    assert 'sum' in result 
    assert result["sum"]==4

def test_difference_operations():
    result=math_operations(1,3)
    assert 'difference' in result 
    assert result["difference"]==-2

def test_product_operations():
    result=math_operations(1,3)
    assert 'product' in result 
    assert result["product"]==3

def test_quotient_operations():
    result=math_operations(1,3)
    assert 'quotient' in result 
    assert result["quotient"]==approx(0.3333333333333333)

def test_quotient_zero_operations():
    result=math_operations(1,0)
    assert 'quotient' in result 
    assert result["quotient"]==None