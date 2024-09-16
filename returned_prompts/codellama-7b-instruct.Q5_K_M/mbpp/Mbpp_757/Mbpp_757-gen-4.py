"""
def count_reverse_pairs(string_list):
    count = 0
    for s in string_list:
        if s[::-1] in string_list:
            count += 1
    return count
"""