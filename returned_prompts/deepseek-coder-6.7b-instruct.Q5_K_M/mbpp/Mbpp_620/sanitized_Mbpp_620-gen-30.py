def largest_subset(arr): 
    n = len(arr) 
    divCount = [1]*n 
    arr.sort() 
    for i in range(1, n): 
        for j in range(i): 
            if arr[i] % arr[j] == 0: 
                divCount[i] = max(divCount[i], divCount[j] + 1) 
    return max(divCount)