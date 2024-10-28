def find_length(s):
    max_diff = 0
    max_zeros = 0
    max_ones = 0
    for i in range(len(s)):
        zeros = s[:i+1].count('0')
        ones = s[:i+1].count('1')
        diff = abs(zeros - ones)
        if diff > max_diff:
            max_diff = diff
            max_zeros = zeros
            max_ones = ones
    return max_diff