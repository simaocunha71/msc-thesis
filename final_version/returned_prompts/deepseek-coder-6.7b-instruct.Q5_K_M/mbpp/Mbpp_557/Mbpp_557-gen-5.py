def toggle_string(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

print(toggle_string("Python"))  # Output: "pYTHON"

"""
Explanation:
This function works by iterating over each character in the input string. If the character is uppercase, it converts it to lowercase and vice versa. The result is a new string where all the characters have been toggled.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
