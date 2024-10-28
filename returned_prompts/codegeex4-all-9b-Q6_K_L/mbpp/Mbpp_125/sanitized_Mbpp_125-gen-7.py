def find_length(binary_string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    
    for char in binary_string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        diff = abs(count_0 - count_1)
        max_diff = max(max_diff, diff)
    
    return max_diff