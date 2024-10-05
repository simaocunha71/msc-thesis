    # This is not a good solution. It doesn't handle nested parens well and is O(n^2) in the number of parens
    # and O(n) in the number of characters. 
    # For example, if the input string is '((( )))', it will not work correctly.

    # We can do this in O(n) time and O(n) space. We can also handle nested parens.
    # We will use a stack to keep track of the groups of parens.
    # For each paren we see, we will push it onto the stack if it's opening paren, and pop it off the stack if it's
    # closing paren. If it's an opening paren, we will also push a placeholder onto the stack.
    # If we see a closing paren and the top of the stack is the placeholder, we will pop the placeholder off the stack
    # and the top of the stack will be the group that we want to return.
    # We will continue to do this until we have no more parens left to process.
    # If the stack is not empty at the end, then there were more closing parens than opening parens, and that's an error.
    # If the stack is empty at the end, then we have successfully extracted all the groups.
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                # We can't pop off an empty stack
                return []
            elif stack[-1] == '(':
                # This is an error, we have more closing parens than opening parens
                return []
            else:
                # This is the end of the group that we want to return
                return_value = stack.pop()[1:]
                stack.pop()
                return [return_value]
        else:
            # We have an error, the input string contains something other than parens
            return []
    # If we get to the end of the function, then the stack is not empty. This means that there were more closing
    # parens than opening parens.
    return []
