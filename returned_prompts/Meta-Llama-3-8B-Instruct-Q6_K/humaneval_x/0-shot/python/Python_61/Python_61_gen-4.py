def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# Test cases:
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False

Explanation:
The function uses a stack to keep track of the opening brackets. For each character in the string, if it's an opening bracket, we push it onto the stack. If it's a closing bracket, we check if the stack is empty. If it is, that means there's no corresponding opening bracket, so we return False. If the stack is not empty, we pop the top element (which should be an opening bracket) and continue. At the end, if the stack is empty, that means every opening bracket had a corresponding closing bracket, so we return True. If the stack is not empty, that means there were opening brackets without corresponding closing brackets, so we return False.