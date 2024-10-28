

def sum_squares(lst):
    return sum(map(lambda x: int(x) ** 2, lst))


print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([1, 4, 9]))  # 98
print(sum_squares([1, 3, 5, 7]))  # 84
print(sum_squares([1.4, 4.2, 0]))  # 29
print(sum_squares([-2.4, 1, 1]))  # 6

# Using list comprehension

def sum_squares(lst):
    return sum([int(x) ** 2 for x in lst])


print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([1, 4, 9]))  # 98
print(sum_squares([1, 3, 5, 7]))  # 84
print(sum_squares([1.4, 4.2, 0]))  # 29
print(sum_squares([-2.4, 1, 1]))  # 6
<jupyter_output>
14
98
84
29
6
<jupyter_text>
Task 2:Write a Python function that takes a string and returns a list of all substrings of that string. The substrings in the returned list should be sorted by length, in ascending order. Note that single characters are also considered substrings.
<jupyter_code>
