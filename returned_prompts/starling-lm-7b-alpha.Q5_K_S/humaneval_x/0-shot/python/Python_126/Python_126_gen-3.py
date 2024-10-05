    # Here's a solution for you
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))



# Here's an explanation of the solution:
# The function `all()` is a built-in Python function that returns `True` if all items in an iterable are true. Otherwise, it returns `False`.
# In this case, we are using it to check if all elements in the list `lst` are in ascending order. We use a generator expression to compare each element with the next one (`lst[i] <= lst[i+1]`). If any comparison is false, `all()` will return `False`. If all comparisons are true, `all()` will return `True`.
# Therefore, the function `is_sorted()` will return `True` if all elements in the list are in ascending order and `False` otherwise.



# Here's a step-by-step breakdown of the solution:
# 1. Define the function `is_sorted(lst)` that takes a list `lst` as an argument.
# 2. Use the `all()` function to check if all elements in the list `lst` are in ascending order. The `all()` function takes a generator expression as an argument that compares each element with the next one (`lst[i] <= lst[i+1]`). If any comparison is false, `all()` will return `False`. If all comparisons are true, `all()` will return `True`.
# 3. Return the result of the `all()` function as the output of the `is_sorted()` function.



# Here's an example usage of the `is_sorted()` function:

def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True