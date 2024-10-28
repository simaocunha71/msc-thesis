    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return len(stack) == 0 and any(string[i] == "[" and string[i+1] == "]" for i in range(len(string)-1))

The function `is_nested` works by iterating through the input string, and each time it encounters an opening bracket, it pushes it onto a stack. It also pops the top element from the stack each time it encounters a closing bracket. If at any point it tries to pop from an empty stack, or if it encounters a closing bracket without a matching opening bracket, it returns False. After iterating through the entire string, it checks if the stack is empty. If it is, and there is at least one valid subsequence of brackets, it returns True. Otherwise, it returns False.

The condition `any(string[i] == "[" and string[i+1] == "]" for i in range(len(string)-1))` checks if there is at least one valid subsequence of brackets. It does this by iterating through the string and checking each pair of adjacent brackets. If it finds a pair of brackets that form a valid subsequence, it returns True. Otherwise, it returns False.

Note that the function assumes that the input string only contains square brackets. If the input string can contain other characters, you would need to modify the function to handle those cases.

Also note that this function only checks for nested brackets. It does not check for brackets that are not nested, or for brackets that are not in the correct order. If you want to check for all of these conditions, you would need a more complex function.
    '''

# Test cases
print(is_nested('[[]]'))  # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))  # ➞ False
print(is_nested('[]'))  #