def sum_squares(lst):
    return sum( math.ceil(num) ** 2 for num in lst)  # Pythonic way

# Alternative
def sum_squares(lst):
    return sum((math.ceil(num)) ** 2 for num in lst)

# Test
print(sum_squares([1,2,3]))  # Output: 14
print(sum_squares([1,4,9]))  # Output: 98
print(sum_squares([1,3,5,7]))  # Output: 84
print(sum_squares([1.4,4.2,0]))  # Output: 29
print(sum_squares([-2.4,1,1]))  # Output: 6

# Explanation:
# The math.ceil() function is used to round each number in the list up to the nearest integer.
# The ** operator is used to square each number.
# The sum() function is used to calculate the sum of the squared numbers.
# The result is the sum of the squared numbers in the list, rounded up to the nearest integer.