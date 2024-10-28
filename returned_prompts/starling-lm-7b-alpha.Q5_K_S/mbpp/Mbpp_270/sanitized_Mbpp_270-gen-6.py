def sum_even_and_even_index(arr):
    s = 0
    for i,n in enumerate(arr):
        if i%2 == 0 and n%2 == 0:
            s += n
    return s