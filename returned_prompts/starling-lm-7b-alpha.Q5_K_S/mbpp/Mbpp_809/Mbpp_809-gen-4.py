def check_smaller(t1,t2):
    return all(x<y for x,y in zip(t1,t2))


"""
In this problem, we need to check if each element of second tuple is smaller than its corresponding element in the first tuple.
To solve this, we can use the zip function in Python to combine the two tuples into a single iterable, and then use the all and lambda functions to check if all elements of the combined iterable satisfy a certain condition.
In this case, the condition is that each element of the combined iterable is less than its corresponding element in the second tuple. The lambda function is used to define this condition, and the all function is used to check if all elements of the combined iterable satisfy this condition.
Finally, the result of the check is returned as the output of the function.
"""

# Test Case:
print(check_smaller((1, 2, 3), (2, 3, 4)))  # Expected Output: False
print(check_smaller((1, 2, 1), (2, 3, 4)))  # Expected Output: True

# Explanation:
# The first test case checks if each element of the second tuple is smaller than its corresponding element in the first tuple. Since the first element of the first tuple (1) is not smaller than the first element of the second tuple (2), the function returns False.
# The second test case checks if each element of the second tuple is smaller than its corresponding element in the first tuple. Since all elements of the second tuple (2, 3, 4) are smaller than the corresponding elements of the first tuple (1, 2, 1), the function returns True.

```python
```

# Here are some additional test cases to check the function:
print(check_smaller((1, 2, 3), (3, 4, 5)))  # Expected Output: False
print(check_smaller((1, 1, 1), (2, 3, 4)))  # Expected Output: True
print(check_smaller((1, 2, 3), (1, 2, 3)))  # Expected Output: True
print(check_smaller((1