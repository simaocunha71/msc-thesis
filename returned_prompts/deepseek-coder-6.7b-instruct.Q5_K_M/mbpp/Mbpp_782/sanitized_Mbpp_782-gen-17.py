def odd_length_sum(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans += ((i+1)*(n-i)+1)//2 * arr[i]
    return ans