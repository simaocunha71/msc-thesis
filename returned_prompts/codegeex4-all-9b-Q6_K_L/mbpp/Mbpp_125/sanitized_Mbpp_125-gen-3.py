def find_length(binary_string):
    max_diff = 0
    count_0s = 0
    count_1s = 0
    
    for char in binary_string:
        if char == '0':
            count_0s += 1
        else:
            count_1s += 1
        
        diff = abs(count_0s - count_1s)
        max_diff = max(max_diff, diff)
    
    return max_diff