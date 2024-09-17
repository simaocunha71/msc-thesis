
def count_Substrings(s): 
    cnt = 0
    for i in range(len(s)): 
        sum = 0
        for j in range(i, len(s)): 
            sum += int(s[j]) 
            if sum == j - i + 1: 
                cnt += 1
    return cnt


