```
def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            stack.pop()
    return not stack
```


The function `correct_bracketing` takes a string `brackets` as input, which is a sequence of parentheses. It checks if every opening bracket has a corresponding closing bracket. The function uses a stack to keep track of the opening brackets. For each character in the string, if it is an opening bracket, it is pushed onto the stack. If it is a closing bracket, the function checks if the stack is empty. If the stack is empty, it means there is no corresponding opening bracket, so the function returns `False`. If the stack is not empty, it pops the opening bracket from the stack. After processing all characters in the string, the function checks if the stack is empty. If the stack is empty, it means every opening bracket has a corresponding closing bracket, so the function returns `True`. If the stack is not empty, it means there are opening brackets without corresponding closing brackets, so the function returns `False`. 





### Example

Let's test the function with some examples:
```
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
These examples demonstrate that the function correctly identifies strings with correct and incorrect bracketing.