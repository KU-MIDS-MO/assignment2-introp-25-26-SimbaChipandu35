from breakdown_time import *

def add_up_time(d):
    total = 0
    for unit in d:
        total += unit * d[unit]
    return total

def test_breakdown_time_valid():
    result = breakdown_time(3675)
    assert result == {3600: 1, 60: 1, 1: 15}
    assert add_up_time(result) == 3675

def test_breakdown_time_exact_hour():
    result = breakdown_time(7200)
    assert result == {3600: 2}
    assert add_up_time(result) == 7200

def test_breakdown_time_zero():
    result = breakdown_time(0)
    assert result == {}
    assert add_up_time(result) == 0

def test_breakdown_time_invalid_type():
    result = breakdown_time("500")
    assert result == -1

def test_breakdown_time_negative():
    result = breakdown_time(-90)
    assert result == -1
