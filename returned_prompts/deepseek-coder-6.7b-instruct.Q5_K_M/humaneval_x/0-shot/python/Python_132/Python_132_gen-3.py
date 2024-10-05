
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return bool(stack)

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True

Explanation:

This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty or the last opening bracket in the stack is not an opening bracket. If either of these cases is true, it returns False. If it's a valid closing bracket, it removes the last opening bracket from the stack.

Finally, it returns True if there are still opening brackets in the stack (which means there were unmatched opening brackets), and False otherwise.

This function works by iterating through the string and adding opening brackets to the stack. When it encounters a closing bracket, it checks if the last item in the stack is an opening bracket and removes it. If the stack is empty or the last item in the stack is not an opening bracket, it returns False. If the stack is not empty after iterating through the string, it means there are unmatched opening brackets and it returns True.

In the end, if there are any unmatched opening brackets left in the stack, it means the string is not properly nested and the function returns True. If there are no unmatched opening brackets left in the stack, it means the string is properly nested and the function returns False.

This function works by using a stack data structure to keep track of the opening brackets and the closing brackets.

The time complexity of this function is O(n