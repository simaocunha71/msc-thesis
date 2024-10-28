def pair_xor_Sum(arr,n):
    s=0
    for i in range(n):
        for j in range(i+1,n):
            s+=arr[i]^arr[j]
    return s