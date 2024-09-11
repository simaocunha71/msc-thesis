def toggle_string(s):
    result = ""
    for c in s:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result


assert toggle_string("Python")==("pYTHON")


"""
The function works by iterating over each character in the string. If the character is uppercase, it is converted to lowercase using the lower() method and appended to the result string. If the character is not uppercase (i.e. it's lowercase), it is converted to uppercase using the upper() method and appended to the result string.

The assert statement at the end of the code is used to test the function by comparing the output of the function with the expected result. If the function works correctly, the assert statement will evaluate to True and no error message will be displayed. Otherwise, an AssertionError will be raised and the error message will be displayed.
"""

"""
The function toggle_string takes a string as input and returns a new string with all the characters in uppercase if they are originally lowercase, and all the characters in lowercase if they are originally uppercase. This is achieved by iterating over each character in the input string and using the upper() and lower() methods to toggle the case of each character. The resulting string is then returned.
"""

"""
The assert statement is used to verify the correctness of the toggle_string function. By comparing the output of the function with the expected result, we can ensure that the function is working correctly. If the function produces the correct result, the assert statement will evaluate to True and no error message will be displayed. If the function produces an incorrect result, an AssertionError will be raised and an error message will be displayed, indicating that the function is not working correctly.
"""


def toggle_string(s):
    result = ""
    for c in s:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result


assert toggle_string("Python")==("pYTHON")


"""
To test the toggle_string function, we can use the assert statement to compare the output of the function with the expected result. In this case,