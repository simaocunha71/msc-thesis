
def count_Substrings(s): 
    counter = 0
    for i in range(len(s)): 
        sum = 0
        for j in range(i, len(s)): 
            sum += int(s[j]) 
            if sum == j - i + 1: 
                counter += 1
    return counter 


