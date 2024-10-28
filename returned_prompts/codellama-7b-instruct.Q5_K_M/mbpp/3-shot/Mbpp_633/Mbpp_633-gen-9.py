
def pair_xor_Sum(arr, n): 
  
    # Initialize result 
    result = 0; 
  
    # Traverse the array 
    for i in range(0, n): 
        for j in range(i+1, n): 
            result = result + (arr[i] ^ arr[j]); 
  
    return result; 


