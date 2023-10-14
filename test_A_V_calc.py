'''
test_A_V_calc.py

This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

#Imported calculator functions and classes
from A_V_calc_starter import Calculator, calculate_area_volume_1, calculate_area_volume_2, calculate_area_volume_3, calculate_area_volume_4, calculate_area_volume_5 

#Pytest for each calculation function (with some rather "agressive" checks)
def test_calculate_area_volume_1():
    assert calculate_area_volume_1(2, 2) == 4
    assert calculate_area_volume_1(0, 0) == 0
    assert calculate_area_volume_1(5, 5) == 25
    
def test_calculate_area_volume_2():
    assert calculate_area_volume_2(2, 2) == 8
    assert calculate_area_volume_2(0, 0) == 0
    assert calculate_area_volume_2(5, 5) == 125
    
def test_calculate_area_volume_3():
    assert calculate_area_volume_3(2, 2) == 12.566370614359172
    assert calculate_area_volume_3(0, 0) == 0
    assert calculate_area_volume_3(5, 5) == 78.53981633974483
    
def test_calculate_area_volume_4():
    assert calculate_area_volume_4(2, 2) == 33.510321638291124
    assert calculate_area_volume_4(0, 0) == 0
    assert calculate_area_volume_4(5, 5) == 523.5987755982989
    
def test_calculate_area_volume_5():
    assert calculate_area_volume_5(2, 2) == 2
    assert calculate_area_volume_5(0, 0) == 0
    assert calculate_area_volume_5(5, 5) == 12.5



#Runs pytest
if __name__ == "__main__":
    import pytest

