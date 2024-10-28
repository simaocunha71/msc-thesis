
def double_the_difference(lst):
    return sum(n**2 for n in lst if n > 0 and isinstance(n, int) and n%2 == 1)

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0

# The time complexity of this code is O(n), where n is the length of the list.
# The space complexity of this code is O(1), because no additional space is used that scales with the input size.
<jupyter_output>
10
0
81
0
0
<jupyter_text>
Question 3
<jupyter_code>
