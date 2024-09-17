
def max_Product(arr):
    n = len(arr)
    if n == 0:
        return (0,0)
    max1 = arr[0]
    max2 = arr[0]
    min1 = arr[0]
    min2 = arr[0]
    for i in range(1, n):
        if arr[i] >= max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] >= max2:
            max2 = arr[i]
        
        if arr[i] <= min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] <= min2:
            min2 = arr[i]
    return (max1*max2, min1*min2)


