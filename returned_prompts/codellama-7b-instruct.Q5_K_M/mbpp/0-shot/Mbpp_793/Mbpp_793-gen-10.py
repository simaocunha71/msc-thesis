def last(arr,ele):
    if ele in arr:
        return len(arr) - arr[::-1].index(ele) - 1
    else:
        return -1
