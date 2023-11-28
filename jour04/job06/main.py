def swap():
    L=[1,2,3,4,5]
    print(L)
    a, b = L.index(1), L.index(5)
    L[b], L[a] = L[a], L[b]
    print(L)
    
swap()