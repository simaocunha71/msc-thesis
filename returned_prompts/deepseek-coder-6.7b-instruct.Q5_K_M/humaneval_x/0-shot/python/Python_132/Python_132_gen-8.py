
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
    return any(stack)

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True

Explanation:

This problem can be solved by using a stack. The stack will be used to keep track of the brackets. Whenever we encounter an opening bracket, we push it into the stack. When we encounter a closing bracket, we check the top of the stack. If the top element is an opening bracket, we pop it from the stack. If the stack is empty or the top element is not an opening bracket, we return False. After iterating through all the brackets, if the stack is not empty, that means there is a nested bracket, so we return True.

The function `any(stack)` checks if the stack is not empty, which means there is at least one valid subsequence of brackets that is nested.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the string.
"""

# %%
# 2. Write a Python program to find the longest palindromic substring from a given string.

"""
