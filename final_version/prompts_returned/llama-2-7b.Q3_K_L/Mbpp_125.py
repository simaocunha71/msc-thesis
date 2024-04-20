"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(binary):
    length = len(binary)
    number_zeros = 0
    number_ones = 0
    for idx, char in enumerate(binary):
        if bin(char)[-1] == '1':
            number_ones += 1
        else:
            number_zeros += 1
    
    result = max(number_zeros - number_ones, length - (number_ones + number_zeros))

    return result