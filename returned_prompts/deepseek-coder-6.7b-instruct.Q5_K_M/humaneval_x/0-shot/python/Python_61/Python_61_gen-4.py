
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False



'''
The function correct_bracketing checks for balanced brackets in a given string. It does this by using a stack data structure. 

If the bracket is an opening bracket, it is pushed onto the stack. If it is a closing bracket, the function checks if the stack is empty. 

If the stack is empty, that means there is no corresponding opening bracket for this closing bracket, and the function returns False. 

If the stack is not empty, that means there is a corresponding opening bracket, and the function pops the opening bracket from the stack. 

Finally, the function returns True if the stack is empty, meaning all opening brackets have corresponding closing brackets. If the stack is not empty, that means there are unmatched opening brackets, and the function returns False.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
3.
<jupyter_code>
# Write a Python program that prints the first and last 5 elements of a given list.

def print_elements(lst):
    if len(lst) < 10:
        print("List is too short")
    else:
        print("First 5 elements: ", lst[:5])
        print("Last 5 elements: ", lst[-5:])

# Test the function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print_elements(lst)
<jupyter_output>
First 5 elements