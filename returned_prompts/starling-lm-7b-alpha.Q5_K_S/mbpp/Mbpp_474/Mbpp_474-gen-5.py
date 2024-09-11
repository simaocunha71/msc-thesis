def replace_char(string,old_char,new_char):
    """
    Replace characters in a string.

    Parameters:
        string (str): The string to be replaced.
        old_char (str): The character to be replaced.
        new_char (str): The character to replace with.

    Returns:
        str: The replaced string.
    """
    result = ""
    for char in string:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result

if __name__ == "__main__":
    assert replace_char("polygon",'y','l')==("pollgon")









"""
Explanation:
The function replace_char takes three parameters: string, old_char, and new_char. It initializes an empty string, result. Then it iterates through each character in the input string. If the character is equal to the old_char, it adds the new_char to the result string. Otherwise, it adds the original character to the result string. Finally, it returns the result string, which is the original string with the specified characters replaced.

The provided assert statement tests the function by passing the string "polygon", the character 'y', and the character 'l' as arguments. The expected result is the string "pollgon". The assert statement checks if the actual result of the function call is equal to the expected result, and if not, raises an AssertionError.

In this case, the function correctly replaces all instances of the character 'y' in the string "polygon" with the character 'l', resulting in the string "pollgon". Therefore, the assert statement passes and no error is raised.
"""




















































































































