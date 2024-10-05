```
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) > 0
``` 

This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, it means there is no matching opening bracket, so the function returns False. If the stack is not empty, it pops the opening bracket from the stack. At the end of the function, it checks if the stack is empty or not. If the stack is not empty, it means there are unmatched opening brackets, so the function returns True. If the stack is empty, it means all brackets are matched, so the function returns False. 

For example, for the input '[[]]', the function will push '[' to the stack and then pop it twice. At the end, the stack will be empty, so the function will return False. For the input '[[]][[', the function will push '[' to the stack twice and then pop it twice. Then it will push '[' to the stack again and pop it. At the end, the stack will not be empty, so the function will return True. 

This function has a time complexity of O(n), where n is the length of the input string, because it processes each character in the string once. It also has a space complexity of O(n), because in the worst case, the stack will contain all characters in the string. 