
def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i > 0 and i%2 != 0)

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0

