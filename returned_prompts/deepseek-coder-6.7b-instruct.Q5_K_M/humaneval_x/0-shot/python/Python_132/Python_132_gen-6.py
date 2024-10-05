
def is_nested(string):
    count = 0
    for i in string:
        if i == '[':
            count += 1
        if i == ']':
            count -= 1
        if count > 1:
            return True
    return False

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True

Explanation:

This function works by iterating through each character in the string. If it finds an open bracket '[' it increments the count. If it finds a closed bracket ']' it decrements the count. If the count is ever greater than 1 at any point, it means there is at least one "valid" subsequence where a bracket is nested, so it returns True. If the function finishes iterating through the string without the count ever being greater than 1, it returns False.

In the question, it's stated that the string will only contain square brackets. So we don't need to worry about other characters.
    ''')
<jupyter_output>
<empty_output>
<jupyter_text>
Question 7
<jupyter_code>
print('''
