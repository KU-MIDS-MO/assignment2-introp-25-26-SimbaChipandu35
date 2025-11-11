def swap_ends(L, k):

    if k <= 0 or len(L) == 0 or k > len(L) // 2:
        return L   
    altered_list = L[-k:] + L[k:-k] + L[:k]
    return altered_list

L = [10, 20, 30, 50, 80, 100]
print(swap_ends(L, 2))