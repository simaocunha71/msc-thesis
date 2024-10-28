from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    groups = []
    group = ''
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            group += char
        elif char == ')':
            stack.pop()
            group += char
            if not stack:
                groups.append(group)
                group = ''

    return groups
# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']  # Correct output
# The function works as expected, correctly separating the paren groups into individual strings. It handles both single and multi-level nesting, and ignores any spaces in the input string. The test case provided demonstrates this functionality.
# Time complexity: O(n), where n is the length of the input string. This is because we are iterating over the string once.
# Space complexity: O(n), where n is the length of the input string. This is because in the worst-case scenario, we might end up with a stack of the same size as the input string.
# The function uses a stack to keep track of the nested parentheses, which allows it to correctly separate the groups. This approach ensures that the groups are balanced and not nested within each other. The replace method is used to remove any spaces in the input string, as per the problem requirements. The groups list is used to store the separated groups, which are then returned as the output.  # Correct output
# The function works as expected, correctly separating the paren groups into individual strings. It handles both single and multi-level nesting, and ignores any spaces in the input string. The test case provided demonstrates this functionality. # Time complexity: O(n), where n is the length of the input string. This is because we are iterating over the string once. # Space complexity: O(n), where n is the length of the input string. This is because in the worst-case scenario, we might end up with a stack of the same size as the input string. # The function uses a stack to keep track of the nested parentheses, which allows it to correctly separate the groups. This approach ensures that the groups are balanced and not nested within each other. The replace method is used to remove any spaces in the input string, as per the problem requirements. The groups list is used to store the separated groups, which are then returned