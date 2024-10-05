
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    return not stack

print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))

"""
This function works by using a stack data structure to keep track of the brackets. 
When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, 
it checks if the stack is empty. If the stack is empty, it means there is no corresponding opening bracket for this closing bracket, 
so the function returns False. If there is a corresponding opening bracket, it is popped from the stack. 
After all brackets have been processed, the function checks if the stack is empty. 
If the stack is empty, it means every opening bracket has a corresponding closing bracket, so the function returns True. 
If the stack is not empty, it means there are unmatched opening brackets, so the function returns False.
"""

# End of the solution
<jupyter_output>
False
True
True
False
<jupyter_text>
Question 2
<jupyter_code>
