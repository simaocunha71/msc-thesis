    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                groups.append('')
            else:
                stack.pop()
                if len(stack) == 0:
                    groups.append('')
                else:
                    groups.append(stack[-1])
    return groups

# Test cases:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
print(separate_paren_groups('(((())))'))  # ['(((()))')]
print(separate_paren_groups('( )'))  # ['()']
print(separate_paren_groups('( )( )( )'))  # ['()', '()', '()']
print(separate_paren_groups('(()(())((()))))'))  # ['(()(())((())))]
print(separate_paren_groups('(((())))'))  # ['(((()))']
print(separate_paren_groups('(()(())((()))))'))  # ['(()(())((())))]
print(separate_paren_groups('( )( )( )'))  # ['()', '()', '()']
print(separate_paren_groups('(((())))'))  # ['(((()))']
print(separate_paren_groups('(()(())((()))))'))  # ['(()(())((())))]



# Another solution

def separate_paren_groups(paren_string):
    stack = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                yield ''
            else:
                j = stack.pop()
                yield paren_string[j:i+1]
    if stack:
        raise ValueError('unclosed parentheses')

print(list(separate_paren_groups('( ) (( )) (( )( ))'))) 