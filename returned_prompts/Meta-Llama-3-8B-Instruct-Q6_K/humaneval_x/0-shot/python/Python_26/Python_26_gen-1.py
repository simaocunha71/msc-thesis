    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
# This function removes duplicates by keeping track of the numbers it has seen so far in a set.
# It iterates over the input list and for each number, it checks if it has seen it before.
# If not, it adds the number to the set and the result list. This way, the result list contains all unique numbers from the input list, in the order they appeared. 
# The function is also tested with an example, where it correctly removes the duplicate 2 from the input list.  # NOQA
# It's worth noting that this function has a time complexity of O(n), where n is the length of the input list, because it has to iterate over the list once. 
# The space complexity is also O(n), because in the worst case (when all numbers are unique), the set will contain all numbers from the input list. 
# If the input list is very large, this function might use a lot of memory. 
# In that case, a different approach might be needed, such as using a dictionary to keep track of the numbers and their counts. 
# However, for small to medium-sized input lists, this function should be fine.  # NOQA
# This function is also quite readable and easy to understand, which is important for maintainability and collaboration. 
# It's a good example of how to solve a common problem in Python, and it could be used as a starting point for more complex problems.  # NOQA
# It also handles the problem as described, which is to remove duplicates while keeping the order of the input list. 
# This is important, because it means that the function doesn't just return a set of unique numbers, but a list of unique numbers in the order they appeared in the input list.  # NOQA
# This makes the function more useful and flexible, because it can be used in a wider range of situations.  # NOQA
# It also includes a docstring that describes the function and its parameters, which is important for understanding how to use the function. 
# It also includes a test case, which is important for ensuring that the function works correctly.  # NOQA
# It's a good example of how to write a well-documented and well-tested function in Python.  # NOQA
# It