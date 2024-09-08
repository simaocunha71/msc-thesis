"""
def check_occurences(lst):
    count_dict = {}
    for tup in lst:
        if tup in count_dict:
            count_dict[tup] += 1
        else:
            count_dict[tup] = 1
    return count_dict

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)])) #{(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

