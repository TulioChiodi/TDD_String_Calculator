import pytest
import string_calculator as sc

def test_Add():
    assert sc.Add('') == 0 
    assert sc.Add('1') == 1
    assert sc.Add('80') == 80
    assert sc.Add('100.1') == 100.1
    assert sc.Add('1,2') == 3
    assert sc.Add('10.2,3.3') == 13.5
    assert sc.Add('1\n2') == 3
    assert sc.Add('1\n2\n5') == 8
    assert sc.Add('1,2,4') == 7
    assert sc.Add('1\n2,3') == 6
