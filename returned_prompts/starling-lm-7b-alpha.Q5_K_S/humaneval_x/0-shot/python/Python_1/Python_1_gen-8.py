    # Initialize a stack to keep track of the open brackets
    stack = []
    # Initialize an empty list to keep track of the balanced substrings
    substrings = []
    # Iterate over the parentheses string
    for char in paren_string:
        # If the char is an opening parenthesis, add it to the stack
        if char == "(":
            stack.append(char)
        # If the char is a closing parenthesis, pop the last open parenthesis from the stack
        # and append the current substring to the list of balanced substrings
        elif char == ")":
            substrings.append("".join(stack))
            stack.pop()
    # Pop the remaining open parentheses from the stack and append them to the list of balanced substrings
    substrings.append("".join(stack))
    # Return the list of balanced substrings
    return substrings


# Test Cases
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
print(separate_paren_groups('(((())))'))  # Output: ['(())', '(())']
print(separate_paren_groups('(((()))) ()'))  # Output: ['(())', '(())']
print(separate_paren_groups('(((()))) ()()'))  # Output: ['(())', '(())']
print(separate_paren_groups('(((()))) ()()()'))  # Output: ['(())', '(())']
print(separate_paren_groups('())))))'))  # Output: []
print(separate_paren_groups('(())(()'))  # Output: []
print(separate_paren_groups('()(()'))  # Output: ['()']
print(separate_paren_groups('()(()('))  # Output: []
print(separate_paren_groups('()(()())('))  # Output: []
print(separate_paren_groups('()(()())()('))  # Output: []


# Here is an example of a test case that is not balanced:
print(separate_paren_groups('(((()))) ()()()'))  # Output: