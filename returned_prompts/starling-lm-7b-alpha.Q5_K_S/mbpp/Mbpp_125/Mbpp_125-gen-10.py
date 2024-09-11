"""
def find_length(string):
    max_difference = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            count_zero = string[i:j+1].count('0')
            count_one = string[i:j+1].count('1')
            max_difference = max(max_difference, abs(count_zero - count_one))
    return max_difference

"""
def find_length(string):
    max_difference = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            count_zero = string[i:j+1].count('0')
            count_one = string[i:j+1].count('1')
            max_difference = max(max_difference, abs(count_zero - count_one))
    return max_difference

assert find_length("11000010001") == 6
"""
def find_length(string):
    max_difference = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            count_zero = string[i:j+1].count('0')
            count_one = string[i:j+1].count('1')
            max_difference = max(max_difference, abs(count_zero - count_one))
    return max_difference

assert find_length("11000010001") == 6

# Time complexity : O(n^2)
# Space complexity : O(1)

"""
def find_length(string):
    max_difference = 0
    for i in range(len(string)):
        count_zero = 0
        count_one = 0
        for j in range(i, len(string)):
            if string[j] == '0':
                count_zero += 1
            else:
                count_one += 1
            max_difference = max(max_difference, abs(count_zero - count_one))