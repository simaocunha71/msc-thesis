def len_log(arr):
    max = 0
    for i in range(len(arr)):
        if(len(arr[i])>max):
            max = len(arr[i])
    return max