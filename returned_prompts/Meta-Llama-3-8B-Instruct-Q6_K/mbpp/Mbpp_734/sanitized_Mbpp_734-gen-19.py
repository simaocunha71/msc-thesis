def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    sum_of_subarray_prod = 0
    for i in range(n):
        for j in range(i, n):
            subarray = lst[i:j+1]
            sum_of_subarray_prod += sum(subarray)
    return sum_of_subarray_prod