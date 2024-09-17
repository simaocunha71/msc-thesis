```
def check_expression(expression):
    stack = []
    bracket_map = {"(": ")", "{": "}", "[": "]"}
    for bracket in expression:
        if bracket in bracket_map:
            stack.append(bracket)
        elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
            return False
    return len(stack) == 0
```    
The function `check_expression` checks if the given expression is balanced or not. It uses a stack to keep track of the opening brackets. It iterates over each character in the expression. If it encounters an opening bracket, it pushes it onto the stack. If it encounters a closing bracket, it checks if the stack is empty or the top of the stack does not match the current closing bracket. If either condition is true, it returns `False`. If it finishes iterating over the expression and the stack is empty, it returns `True`; otherwise, it returns `False`. The unit test `assert check_expression("{()}[{}]") == True` ensures that the function works correctly. 

For example, if the input is "{()}[{}]", the function returns `True` because the expression is balanced. If the input is "{([)]}", the function returns `False` because the expression is not balanced. 





