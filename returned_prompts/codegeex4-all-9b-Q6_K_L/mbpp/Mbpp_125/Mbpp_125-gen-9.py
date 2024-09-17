def find_length(binary_string):
    max_length = 0
    for i in range(len(binary_string)):
        count_0 = 0
        count_1 = 0
        for j in range(i, len(binary_string)):
            if binary_string[j] == '0':
                count_0 += 1
            elif binary_string[j] == '1':
                count_1 += 1
            max_length = max(max_length, abs(count_0 - count_1))
    return max_length

