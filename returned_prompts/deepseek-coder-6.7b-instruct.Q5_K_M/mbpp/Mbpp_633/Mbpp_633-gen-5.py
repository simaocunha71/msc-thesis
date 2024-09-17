
def pair_xor_Sum(arr, n): 
  
    sum = 0
    for i in range(0, 32): 
      
        cnt = 0
        for j in range(0, n): 
            if ((arr[j] >> i) & 1): 
                cnt += 1
  
        sum += cnt * (n - cnt) * 2
  
    return sum 


