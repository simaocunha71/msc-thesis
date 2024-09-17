
def sum_Of_Subarray_Prod(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            prod = 1
            for k in range(i, j+1):
                prod *= arr[k]
            total += prod
    return total


