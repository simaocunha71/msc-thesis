def sum_Of_Subarray_Prod(arr): 
    n = len(arr) 
    sum = 0
    for i in range(0,32): 
        sub = [] 
        for j in range(0, n): 
            if ((i & (1 << j)) > 0): 
                sub.append(arr[j]) 
        if len(sub)!=0:
            prod = 1
            for i in sub:
                prod *= i
            sum += prod 
    return sum