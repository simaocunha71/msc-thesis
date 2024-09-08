def sum_of_digits(lst):
    return [sum(int(i) for i in str(n)) for n in lst]

print(sum_of_digits([10,2,56]))

# Explanation:
# The function sum_of_digits takes a list of numbers as input.
# For each number in the list, the function converts the number to a string, then converts each character of the string back to an integer.
# Then it sums up these integers, effectively adding up the digits of the number.
# It returns a list of these sums.
# So for example, sum_of_digits([10,2,56]) returns [1, 2, 11] because 1+0=1, 2+0=2, and 5+6=11.

# Solution 2:
def sum_of_digits(lst):
    return [sum(map(int, str(abs(num))))) for num in lst]

print(sum_of_digits([10,2,56]))

# Explanation:
# In this solution, the function uses the built-in Python function map() to apply the int() function to each character of the string representation of the absolute value of each number in the input list.
# The sum() function then adds up these integers, effectively adding up the digits of the number.
# The function returns a list of these sums.
# The abs() function is used to ensure that the function works correctly with negative numbers.
# So for example, sum_of_digits([10,2,56]) returns [1, 2, 11] because 1+0=1, 2+0=2, and 5+6=11.
<jupyter_output>
[1, 2, 11]
<jupyter_text>
