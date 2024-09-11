"""
def max_difference(tup_list):
    max_diff = 0
    for i in range(len(tup_list)):
        for j in range(i+1, len(tup_list)):
            diff = tup_list[j][0] - tup_list[i][1]
            if diff > max_diff:
                max_diff = diff
    return max_diff

# Unit Test
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
print("All tests passed.")

"""

def max_difference(tup_list):
    max_diff = 0
    for i in range(len(tup_list)):
        for j in range(i+1, len(tup_list)):
            diff = tup_list[j][1] - tup_list[i][0]
            if diff > max_diff:
                max_diff = diff
    return max_diff

# Unit Test
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
print("All tests passed.")






"""
