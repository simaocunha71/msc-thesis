def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

# Test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

# More tests
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], 2, 5) == 21
assert sum_range_list([0,1,2,3,4,5,6,7,8,9], 0, 9) == 45

# Edge cases
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], 0, 0) == 1
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], 9, 9) == 10
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], -1, 9) == 46

# Random test
import random
lst = [random.randint(0,10) for _ in range(20)]
start = random.randint(0,19)
end = random.randint(start,19)
print(f"List: {lst}")
print(f"Start: {start}")
print(f"End: {end}")
print(f"Sum: {sum_range_list(lst, start, end)}")



"""
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

# Test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

# More tests
assert sum_range_list([1,2,3,4,5,6,7,8,9,10], 2, 5)