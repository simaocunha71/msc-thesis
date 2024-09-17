
def pair_xor_Sum(arr, n):
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += arr[i] ^ arr[j]
    return ans


