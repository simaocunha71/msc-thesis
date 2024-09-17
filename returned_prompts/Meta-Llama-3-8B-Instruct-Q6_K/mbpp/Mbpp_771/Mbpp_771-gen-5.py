```
def check_expression(expression):
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}
    for char in expression:
        if char in mapping:
            stack.append(char)
        elif len(stack) == 0 or mapping[stack.pop()] != char:
            return False
    return len(stack) == 0
```


In this function, we use a stack to keep track of the opening brackets. When we encounter a closing bracket, we check if the stack is empty or the top of the stack does not match the current closing bracket. If either condition is true, we return False, indicating that the expression is not balanced. At the end, we check if the stack is empty. If it is, we return True, indicating that the expression is balanced. Otherwise, we return False. 

The unit test `assert check_expression("{()}[{}]") == True` passes because the expression "{()}[{}]" is balanced. The stack would be ["{", "(", "["] and at the end, it would be empty, indicating that the expression is balanced. 

Note that this function only works for expressions with parentheses, brackets, and curly braces. If you need to support other types of brackets, you would need to add them to the mapping dictionary. 