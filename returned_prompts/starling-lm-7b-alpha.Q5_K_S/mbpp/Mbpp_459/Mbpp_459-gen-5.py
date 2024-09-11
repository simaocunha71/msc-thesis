def remove_uppercase(s):
    return "".join([c for c in s if c.islower()])

# Test
print(remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos')  # True






"""
Explanation:
To solve this problem, we can iterate through the string and check if each character is uppercase. If it is not uppercase, we add it to a new string. Finally, we return the new string without any uppercase characters.
The provided solution uses a list comprehension to iterate through the string and checks if each character is lowercase using the islower() method. If the character is lowercase, it is added to a new list. Finally, we use the join() method to convert the list of characters back into a string.
"""

"""
In Python, the islower() method is a built-in method for strings that returns True if all the characters in the string are lowercase and False if any character is uppercase. We can use this method to check if each character in the string is lowercase.
"""

"""
The join() method is also a built-in method in Python that concatenates all the elements in a list into a single string. It is called on the string and takes a list as an argument. In this case, we use an empty string as the separator between the characters in the list.
"""

"""
By using a list comprehension, we can perform the iteration and conditional check in a single line of code. The list comprehension iterates through each character in the string and checks if it is lowercase using the islower() method. If the character is lowercase, it is added to the list. Finally, we use the join() method to convert the list of characters back into a string.
"""

"""
The assert statement is used to check if a condition is true. In this case, we use the assert statement to check if the result of the remove_uppercase() function is equal to the expected output 'cstyoravoitshos'. If the condition is true, the assert statement does nothing. Otherwise, it raises an AssertionError with an error message describing the expected and actual results.
"""

"""
The provided solution correctly removes