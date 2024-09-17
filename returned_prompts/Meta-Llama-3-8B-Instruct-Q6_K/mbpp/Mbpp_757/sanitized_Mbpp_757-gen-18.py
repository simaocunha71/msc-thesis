def count_reverse_pairs(lst):
    reversed_strings = {}
    count = 0
    for s in lst:
        reversed_string = s[::-1]
        if reversed_string in reversed_strings:
            count += 1
        else:
            reversed_strings[s] = s[::-1]
    return count // 2