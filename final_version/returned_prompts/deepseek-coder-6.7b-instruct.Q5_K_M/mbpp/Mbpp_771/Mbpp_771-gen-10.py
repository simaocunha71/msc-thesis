
def check_expression(exp):
    stack = []
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    for i in exp:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and (open_brackets[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(check_expression("{()}[{}]"))

# Output: True

"""
The function check_expression uses a stack to keep track of opening brackets. As it encounters a closing bracket, it checks if the last opening bracket matches the type of the closing bracket. If it does, then it pops the opening bracket from the stack. If at the end, the stack is empty, it means the expression is balanced.
"""
<jupyter_output>
True
<jupyter_text>
Question 4:
<jupyter_code>
