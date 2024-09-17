def find_length(binary_string):
    max_diff = 0
    count_zero = 0
    count_one = 0

    for i in range(0, len(binary_string)):

        if binary_string[i] == '0':
            count_zero += 1

        if binary_string[i] == '1':
            count_one += 1

        if count_zero > count_one:
            diff = count_zero - count_one
        else:
            diff = count_one - count_zero

        if diff > max_diff:
            max_diff = diff

        if count_zero < count_one:
            count_zero = 0
        else:
            count_one = 0

    return max_diff