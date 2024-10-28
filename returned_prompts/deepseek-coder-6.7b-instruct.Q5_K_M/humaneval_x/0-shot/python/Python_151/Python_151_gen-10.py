
def double_the_difference(lst):
    return sum(n**2 for n in lst if isinstance(n, int) and n > 0 and n % 2 == 1)

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0

# Explanation:
# In the first case, 1, 3 and 9 are the squares of the positive odd numbers.
# In the second case, there are no positive odd numbers, so we return 0.
# In the third case, 9 is the only positive odd number, so we return 9*9 = 81.
# In the fourth case, there are no numbers, so we return 0.
# In the fifth case, there are no numbers, so we return 0.
