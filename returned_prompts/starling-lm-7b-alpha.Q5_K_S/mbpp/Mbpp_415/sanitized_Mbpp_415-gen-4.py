def max_Product(arr):
    res = []
    arr.sort()
    if len(arr)<3:
        return arr[0],arr[1]
    else:
        for i in range(len(arr)-2,0,-1):
            if arr[i] * arr[0] * arr[-1] > res[0]:
                res = [arr[i],arr[0],arr[-1]]
            if arr[i] * arr[0] * arr[-1] < res[0]:
                break
        return res[0],res[1]