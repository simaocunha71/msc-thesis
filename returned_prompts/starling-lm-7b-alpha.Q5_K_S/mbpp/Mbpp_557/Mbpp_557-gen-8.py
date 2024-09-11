def toggle_string(string):
    """
    >>> toggle_string("Python")
    "pYTHON"
    """
    # Toggle the case of all characters in a string
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()












"""
To toggle the case of all characters in a string, we can create a function that iterates over each character in the string. We can then use the islower() and isupper() methods to check the case of each character. If the character is lowercase, we can convert it to uppercase using the upper() method. If the character is uppercase, we can convert it to lowercase using the lower() method. If the character is neither lowercase nor uppercase, we can simply append it to the result string. Finally, we can return the result string.
"""

"""
In the provided code, the toggle_string() function takes a string as input and initializes an empty string called result. It then iterates over each character in the input string using a for loop. For each character, it checks if it is lowercase using the islower() method. If it is lowercase, it converts it to uppercase using the upper() method and appends it to the result string. If it is uppercase, it converts it to lowercase using the lower() method and appends it to the result string. If the character is neither lowercase nor uppercase, it simply appends it to the result string. Finally, it returns the result string.

The doctest module is used to test the code. The assert statement checks if the result of the toggle_string() function with the input "Python" is equal to "pYTHON". If the assert statement passes, the test is successful. Otherwise, an error message is raised.
"""

"""
To use the toggle_string() function, you can call it with a string as an argument. For example, toggle_string("Python") will return "pY