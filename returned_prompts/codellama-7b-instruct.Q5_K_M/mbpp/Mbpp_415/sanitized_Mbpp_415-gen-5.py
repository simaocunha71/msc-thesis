def max_Product(arr):
    prod = 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            prod = max(prod, arr[i]*arr[j])
    return prod