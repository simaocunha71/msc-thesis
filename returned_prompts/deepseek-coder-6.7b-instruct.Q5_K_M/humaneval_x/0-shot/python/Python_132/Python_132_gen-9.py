
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        else:
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True

Explanation:

The function is_nested takes a string as input. It initializes an empty list stack.
It then iterates over the input string character by character. If the character is an opening bracket '[', it adds it to the stack.
If the character is a closing bracket ']', it checks if the stack is empty or the last element of the stack is not an opening bracket '['.
If either of these conditions is true, it returns False. If not, it removes the last element from the stack.
After iterating over all characters in the input string, it checks if the length of the stack is 0. If it is, it returns True, otherwise it returns False.
'''

# 2.

'''
