
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    prod = [0]*n
    sum_prod = 0
    for i in range(n):
        if i == 0:
            prod[i] = lst[i]
        else:
            prod[i] = lst[i] * lst[i-1]
    for i in range(n):
        sum_prod += prod[i]
    return sum_prod


