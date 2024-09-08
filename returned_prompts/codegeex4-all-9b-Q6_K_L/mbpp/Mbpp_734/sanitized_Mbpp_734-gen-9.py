def sum_Of_Subarray_Prod(arr):
    sum_of_products = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j+1):
                product *= arr[k]
            sum_of_products += product
    return sum_of_products