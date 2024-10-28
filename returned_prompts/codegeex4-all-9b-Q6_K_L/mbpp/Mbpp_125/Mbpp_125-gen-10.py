def find_length(binary_string):
    count_0s = binary_string.count('0')
    count_1s = binary_string.count('1')
    max_diff = abs(count_0s - count_1s)
    for i in range(len(binary_string)):
        for j in range(i+1, len(binary_string)+1):
            sub_string = binary_string[i:j]
            count_0s_sub = sub_string.count('0')
            count_1s_sub = sub_string.count('1')
            diff = abs(count_0s_sub - count_1s_sub)
            max_diff = max(max_diff, diff)
    return max_diff

