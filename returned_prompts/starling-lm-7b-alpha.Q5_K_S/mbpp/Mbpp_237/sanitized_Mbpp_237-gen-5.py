def check_occurences(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
arr = [3, 1, 1, 3, 2, 5, 5, 2, 6, 3]