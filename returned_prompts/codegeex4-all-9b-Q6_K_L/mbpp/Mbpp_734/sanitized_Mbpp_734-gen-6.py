def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            subarray = lst[i:j+1]
            product = 1
            for num in subarray:
                product *= num
            total_sum += product
    return total_sum