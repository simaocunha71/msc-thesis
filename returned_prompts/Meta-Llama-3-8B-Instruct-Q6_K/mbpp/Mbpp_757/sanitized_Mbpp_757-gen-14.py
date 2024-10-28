def count_reverse_pairs(lst):
    count = 0
    for string in lst:
        for other_string in lst:
            if string != other_string and string == other_string[::-1]:
                count += 1
    return count