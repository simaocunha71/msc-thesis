
def count_Pairs(arr):
    n = len(arr)
    ans = 0
    count = [0] * (max(arr)+1)
    for i in range(n):
        count[arr[i]] += 1
    for i in range(max(arr)+1):
        ans += count[i]*(count[i]-1)//2
    return ans


