def pair_xor_Sum(arr,n):
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            sum = sum + arr[i]^arr[j]
    return sum