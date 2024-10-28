    """
    This question can be solved using stack.
    """

    # The stack is used to keep track of the deepest level of nesting of parentheses in the current group.
    # At the beginning of each group, the stack is empty.
    # For each of the character in the string, if the character is '(', push 1 to the stack.
    # If the character is ')', pop the stack and increase the count by 1.
    # After parsing all characters in the string, the stack should be empty.
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            count = stack.pop()
            if len(stack) == 0:
                result.append(count)
            else:
                stack[-1] += count
    if len(stack) != 0:
        raise Exception("Error")
    return result
