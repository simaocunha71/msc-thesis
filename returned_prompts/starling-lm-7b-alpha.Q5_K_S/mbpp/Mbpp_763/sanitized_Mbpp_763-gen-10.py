def find_min_diff(arr,val):
    arr = sorted(arr)
    diff = 99999999999999999999999999999999999
    for i in range(len(arr)):
        diff = min(diff,abs(arr[i]-val))
    return diff