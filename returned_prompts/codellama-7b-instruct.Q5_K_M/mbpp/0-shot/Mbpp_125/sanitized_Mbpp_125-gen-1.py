def find_length(binary_string):
    count = 0
    max_count = 0
    for i in range(len(binary_string)):
        if binary_string[i] == "0":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count