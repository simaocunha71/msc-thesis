from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]
# 
# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc'] 
print(all_prefixes('abcd'))  # Output: ['a', 'ab', 'abc', 'abcd']
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes(''))  # Output: [] 
# 
# Explanation:
# The function uses list comprehension to generate all prefixes of the input string.
# It does this by slicing the string from the beginning to the current index i.
# The range function is used to generate all possible indices from 1 to the length of the string.
# The result is a list of all prefixes in order from shortest to longest. 
# The function handles the edge case where the input string is empty by returning an empty list. 
# The function also handles the edge case where the input string is 'a' by returning ['a']. 
# The function handles the edge case where the input string is 'abc' by returning ['a', 'ab', 'abc']. 
# The function handles the edge case where the input string is 'abcd' by returning ['a', 'ab', 'abc', 'abcd']. 
# The function is efficient because it has a time complexity of O(n), where n is the length of the input string. 
# The function is also easy to understand and use. 
# 
# Note: The function does not handle the case where the input string is None. 
# It would be a good idea to add a check at the beginning of the function to handle this case. 
# The function could return an empty list or raise an exception, depending on the desired behavior. 
# 
# Also, the function does not handle the case where the input string is not a string. 
# It would be a good idea to add a check at the beginning of the function to handle this case. 
# The function could return an empty list or raise an exception, depending on the desired behavior. 
# 
# It would also be a good idea to add some documentation to the function to explain what it