def pair_xor_Sum(arr,n):
    return sum([arr[i]^arr[j] for i in range(n) for j in range(i+1,n)])