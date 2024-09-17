def reverse_Array_Upto_K(arr,k):
    for i in range(int(len(arr)/2)):
        if k>i:
            arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
        else:
            break
    return arr