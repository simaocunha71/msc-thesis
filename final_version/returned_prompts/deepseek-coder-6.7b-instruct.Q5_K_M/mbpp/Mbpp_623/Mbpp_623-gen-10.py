def nth_nums(num_list, n):
    return [i ** n for i in num_list]

print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# This function works by using a list comprehension to create a new list. The expression `i ** n` raises the number `i` to the power `n`. The resulting list is returned.

# Alternatively, you can use the built-in Python function `map()` to achieve the same result.

def nth_nums(num_list, n):
    return list(map(lambda x: x ** n, num_list))

print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# This function works by applying the lambda function to each element of the list. The lambda function raises the number to the power `n`. The resulting map object is converted back into a list and returned.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 10
<jupyter_code>
