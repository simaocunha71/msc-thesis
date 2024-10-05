
def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join([char.upper() if char.islower() else char.lower() for char in s])

print(solve("1234")) # "4321"
print(solve("ab")) # "AB"
print(solve("#a@C")) # "#A@c"
print(solve("Hello")) # "oLlEh"
print(solve("PYTHON")) # "python"
print(solve("12345")) # "54321"

Explanation:

First, the function checks if there are any alphabetic characters in the string. If there aren't, it reverses the string. If there are, it iterates over each character in the string. If the character is lowercase, it changes it to uppercase and vice versa. Finally, it joins all the modified characters together into a single string and returns it.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2Given a string s and a character c, find the number of occurrences of the character c in the string s.The function should return the number of occurrences.Examples:count_char("Hello","l") = 2count_char("Hello","e") = 1count_char("Hello","x") = 0
<jupyter_code>
