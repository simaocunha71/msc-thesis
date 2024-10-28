def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            result += prod(lst[i:j+1])
    return result
def prod(lst):
    res = 1
    for num in lst:
        res *= num
    return res