"""
def find_Odd_Pair(arr, n) : 
    count = 0; 
    for (int i = 0; i < n; i++) 
        for (int j = i + 1; j < n; j++) 
            if (arr[i]^arr[j] == 1) 
                count++; 
    return count; 
"""