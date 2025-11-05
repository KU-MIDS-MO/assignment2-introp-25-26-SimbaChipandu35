from has_adjacent_duplicate import *

def test_adjacent_1():
    L = [1, 2, 3, 4]
    assert has_adjacent_duplicate(L) == False

def test_adjacent_2():
    L = [5, 5, 2, 1]
    assert has_adjacent_duplicate(L) == True

def test_adjacent_3():
    L = [1, 2, 2, 3, 4]
    assert has_adjacent_duplicate(L) == True

def test_adjacent_4():
    L = [1]
    assert has_adjacent_duplicate(L) == False

def test_adjacent_5():
    L = []
    assert has_adjacent_duplicate(L) == False

def test_non_adjacent_duplicate():
    L = [1, 2, 3, 4, 2]
    assert has_adjacent_duplicate(L) == False
        

