def has_adjacent_duplicate(L):
   
    if len(L)< 2:
        return False
    for k in range (len(L)-1):
               if L[k] == L[k + 1]:
                 return True
    return False 
L=[1,3,4,6]
print(has_adjacent_duplicate(L))
