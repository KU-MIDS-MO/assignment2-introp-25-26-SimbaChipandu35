from swap_ends import *

def test_swap_ends_basic():
    L = [1, 2, 3, 4, 5, 6]
    M = L.copy()
    new_list, num_swaps = swap_ends(L, 2)
    assert new_list == [5, 6, 3, 4, 1, 2]
    assert L == M
    assert num_swaps == 2

def test_swap_ends_k1():
    L = ["a", "b", "c", "d"]
    M = L.copy()
    new_list, num_swaps = swap_ends(L, 1)
    assert new_list == ["d", "b", "c", "a"]
    assert L == M
    assert num_swaps == 1

def test_swap_ends_k_large():
    # k larger than half the list: shold do nothing
    L = [10, 20, 30, 40, 50]
    M = L.copy()
    new_list, num_swaps = swap_ends(L, 3)
    assert new_list == M
    assert L == M
    assert num_swaps == 0

def test_swap_ends_zero_or_empty():
    L = []
    new_list, num_swaps = swap_ends(L, 2)
    assert new_list == []
    assert num_swaps == 0

    L2 = [1, 2, 3]
    M2 = L2.copy()
    new2, swaps2 = swap_ends(L2, 0)
    assert new2 == M2
    assert swaps2 == 0
    assert L2 == M2

def test_swap_ends_singleton():
    L = [7]
    M = L.copy()
    new_list, num_swaps = swap_ends(L, 5)
    assert new_list == [7]
    assert num_swaps == 0
    assert L == M
    
