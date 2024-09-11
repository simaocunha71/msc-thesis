def capital_words_spaces(string):
    """
    Input: string
    Output: string
    """
    result = []
    for i in range(len(string)):
        if i == 0:
            result.append(string[i])
        elif string[i-1] == ' ' and string[i] >= 'A' and string[i] <= 'Z':
            result.append(' ')
            result.append(string[i])
        else:
            result.append(string[i])
    return ''.join(result)

# Test
assert capital_words_spaces("Python") == "Python"
assert capital_words_spaces("PythonIsFun") == "Python IsFun"
assert capital_words_spaces("PythonIsReallyFun") == "Python IsReallyFun"
assert capital_words_spaces("HelloWorld") == "Hello World"
assert capital_words_spaces("JavaScript") == "JavaScript"
assert capital_words_spaces("JavaScriptIsCool") == "JavaScript IsCool"
assert capital_words_spaces("CodingIsFun") == "Coding IsFun"



# Author: _Mumbun_
# Date: 2020-09-18 22:57:28.704784
# Problem: https://www.codewars.com/kata/58a33f9c06c10f7f7f000069/train/python
# Time: O(n)
# Space: O(n)

"""
Explanation:
We can start by initializing an empty list to store the result string. Then, we can iterate through the string, checking if the previous character is a space and the current character is a capital letter. If this is the case, we add a space to the result string and append the current character. Otherwise, we just append the current character. Finally, we join the characters in the result list to form the final result string.

We can use the 'assert' keyword to check if the function works correctly by comparing the output of the function with the expected result.
"""

"""
Ex