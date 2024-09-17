
def find_Odd_Pair(arr, n): 
    ans = 0
    for i in range(0, 32): 
        cnt = 0
        for j in range(0, n): 
            if ((arr[j] >> i) & 1): 
                cnt += 1
        ans += cnt * (n - cnt) 
    return int(ans / 2) 


