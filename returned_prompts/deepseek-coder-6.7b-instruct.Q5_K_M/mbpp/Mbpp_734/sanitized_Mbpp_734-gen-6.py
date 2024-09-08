def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_prod = 0
    for i in range(n):
        if i == 0:
            prod[i] = arr[i]
        else:
            prod[i] = prod[i-1]*arr[i]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l
            if l == 1:
                sum_prod += arr[i]
            else:
                if i == 0:
                    sum_prod += prod[j-1]
                else:
                    sum_prod += prod[j-1]//prod[i-1]
    return sum_prod