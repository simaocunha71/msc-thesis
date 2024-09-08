def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(32))
print(is_power_of_two(64))
print(is_power_of_two(128))
print(is_power_of_two(130))

"""
Write a python function to find the unique elements in a list.
assert unique_elements([1,2,2,3,3,4,4,4,5,5,5,5]) == [1,2,3,4