def sum_Of_Subarray_Prod(lst):
    s = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)+1):
            s += sum(lst[i:j])
    return s