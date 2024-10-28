def sum_Of_Subarray_Prod(lst):
    l = len(lst)
    if l == 0:
        return 0
    if l == 1:
        return lst[0]
    if l == 2:
        return lst[0]*lst[1] + lst[1]*lst[0]
    return sum([lst[i]*lst[j]*lst[k] for i in range(l) for j in range(i+1,l) for k in range(j+1,l)])