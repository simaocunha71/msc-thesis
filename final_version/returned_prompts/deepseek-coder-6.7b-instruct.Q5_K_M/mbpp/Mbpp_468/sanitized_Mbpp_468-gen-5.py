def max_product(arr):
    if len(arr)==0:
        return 0
    max_prod = [0]*len(arr)
    max_prod[0] = arr[0]
    for i in range(1, len(arr)):
        max_prod[i] = max(arr[i], max_prod[i-1]*arr[i])
    return max(max_prod)