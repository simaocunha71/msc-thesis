def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result += reduce(lambda a, b: a*b, lst[i:j])
    return result