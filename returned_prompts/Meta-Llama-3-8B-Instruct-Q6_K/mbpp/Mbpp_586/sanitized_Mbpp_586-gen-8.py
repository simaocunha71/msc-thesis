def split_Arr(arr,n):
    if n > len(arr):
        return arr
    else:
        return arr[n:] + arr[:n]  # slicing the list into two parts and then reversing the first part and adding to the end of the second part.   