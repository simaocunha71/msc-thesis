    def find_separate_groups(paren_string):
        """ Helper function to find the separate_groups of nested parentheses in the string. Return a list of
        starting and ending indexes of the balanced groups.
        """
        groups = []
        stack = []
        for i, char in enumerate(paren_string):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    if paren_string[stack.pop()] == '(':
                        groups.append([stack[-1], i])
                else:
                    groups.append([i, i])
        return groups

    def separate_groups(paren_groups):
        """ Helper function to separate the parentheses groups in the list of indexes.
        """
        separated_groups = []
        for group in paren_groups:
            if group[0] == group[1]:
                separated_groups.append(paren_string[group[0]])
            else:
                separated_groups.append(paren_string[group[0]:group[1]+1])
        return separated_groups

    paren_string = paren_string.replace(' ', '')
    paren_groups = find_separate_groups(paren_string)
    return separate_groups(paren_groups)


# Here are some test cases to validate your function

print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
print(separate_paren_groups('((()))'))  # ['((()))']
print(separate_paren_groups('(()((()))())'))  # ['(()', '(())', '()']
print(separate_paren_groups('(((())))))'))  # ['((()))')
print(separate_paren_groups('(()(())))'))  # ['(())', '()']
print(separate_paren_groups('(((())))'))  # ['((())')
print(separate_paren_groups(''))  # []


# Here are some test cases with extra spaces to validate your function correctly ignores them:
print(separate