def count_reverse_pairs(string_list):
    count = 0
    for string in string_list:
        if string == string[::-1]:
            count += 1
    return count