def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += prod(lst[i:j+1])
    return total_sum
def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result