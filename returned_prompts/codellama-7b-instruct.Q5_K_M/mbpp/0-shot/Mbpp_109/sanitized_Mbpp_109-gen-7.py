def odd_Equivalent(binary_string, rotate_count):
    binary_string_list = list(binary_string)
    for i in range(rotate_count):
        binary_string_list.insert(0, binary_string_list.pop())
    count = 0
    for i in binary_string_list:
        if int(i) == 1:
            count += 1
    return count