def find_length(s):
    max_diff = 0
    max_zeros = 0
    max_ones = 0
    current_zeros = 0
    current_ones = 0
    
    for char in s:
        if char == '0':
            current_zeros += 1
            current_ones = 0
        else:
            current_zeros = 0
            current_ones += 1
        
        max_diff = max(max_diff, abs(current_zeros - current_ones))
        max_zeros = max(max_zeros, current_zeros)
        max_ones = max(max_ones, current_ones)
    
    return max_diff