def sum_range_list(lst, start, end):
    return sum(lst[i] for i in range(start, end + 1))

# Testing
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

# More Testing
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], 0, 9) == 45

# Even More Testing
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], -1, 9) == 45

# Stress Testing
assert sum_range_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], 0, 30) == 420

# One more for good measure...
assert sum_range_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], -10, 29) == 420

# And one last one...
assert sum_range_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], -40, 39) == 420

# And one last one