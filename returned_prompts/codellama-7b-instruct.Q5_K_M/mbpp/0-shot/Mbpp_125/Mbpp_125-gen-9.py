"""
def find_length(binary_string):
    # Your code here
    count_zeroes = 0
    count_ones = 0
    max_diff = 0

    for char in binary_string:
        if char == '0':
            count_zeroes += 1
        else:
            count_ones += 1

        max_diff = max(max_diff, count_ones - count_zeroes)

    return max_diff
"""
