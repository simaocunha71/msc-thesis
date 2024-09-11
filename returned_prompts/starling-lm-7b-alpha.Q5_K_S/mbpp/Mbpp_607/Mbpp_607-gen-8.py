def find_literals(string, pattern):
    # Your code here
    import re
    return re.search(pattern, string).group(), re.search(pattern, string).start(), re.search(pattern, string).end()


# Running code to test the above function
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)




"""
The regex module is a standard module in python. Here is the documentation for the search function.

The function returns a Match object if the string is a match for the regular expression, None if it is not. The returned Match object has three attributes start() and end() that return the start and end index of the match in the string, and group() that returns the actual string that matched.
"""

"""
The above code defines a function find_literals that takes two parameters, string and pattern. The function uses the regex.search function to search the string for the pattern. If the pattern is found in the string, the function returns a tuple of the matched substring, the start index, and the end index. If the pattern is not found, the function returns None.
"""

"""
In the provided assert statement, the function find_literals is called with the string "The quick brown fox jumps over the lazy dog." and the pattern "fox". The expected result is the string "fox", the start index 16, and the end index 19. The assert statement checks that the actual result of the function call matches the expected result.
"""

"""
To use the function find_literals, you can call it with a string and a pattern, and it will return the matching substring, start index, and end index. For example, you can call the function with the string "The quick brown fox jumps over the lazy dog." and the pattern "fox" to find the position of the word "fox" in the string. The function will return the string "fox", the start index 16, and the end index 19, indicating that the word "fox" is located between positions 16 and 19 in the string.
"""



# Python code to define the function.


def find_literals(string, pattern):
   