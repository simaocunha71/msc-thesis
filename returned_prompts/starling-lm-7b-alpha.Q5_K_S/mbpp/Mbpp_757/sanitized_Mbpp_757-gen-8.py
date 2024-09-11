def count_reverse_pairs(s_list):
    """
    Count the pairs of reverse strings in the given string list.
    """
    count = 0
    for s in s_list:
        rev = s[::-1]
        if rev in s_list and s != rev:
            count += 1
    return count