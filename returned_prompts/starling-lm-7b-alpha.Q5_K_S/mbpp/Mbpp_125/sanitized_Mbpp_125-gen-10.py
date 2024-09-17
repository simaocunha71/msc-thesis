def find_length(string):
    max_difference = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            count_zero = string[i:j+1].count('0')
            count_one = string[i:j+1].count('1')
            max_difference = max(max_difference, abs(count_zero - count_one))
    return max_difference