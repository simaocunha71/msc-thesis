def find_length(s):
    max_len = 0
    cur_len = 0
    count_0 = 0
    count_1 = 0
    
    for i in range(len(s)):
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        cur_len = abs(count_1 - count_0)
        
        if cur_len > max_len:
            max_len = cur_len
    
    return max_len