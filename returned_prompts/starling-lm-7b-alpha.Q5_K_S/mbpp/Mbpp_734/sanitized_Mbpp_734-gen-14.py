def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            result += reduce(lambda x,y:x*y, lst[i:j+1])
    return result