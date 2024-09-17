def find_Odd_Pair(arr, n): 
    odd_count = 0
    for i in range(0, 32): 
        cnt = 0
        for j in range(0, n): 
            if ((arr[j] >> i) & 1): 
                cnt += 1
        odd_count += cnt * (n - cnt) 
    return odd_count