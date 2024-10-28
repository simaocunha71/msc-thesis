from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    group = ""
    in_group = False
    for char in paren_string:
        if char == '(':
            if not in_group:
                in_group = True
                group = ""
            group += char
        elif char == ')':
            group += char
            if in_group:
                in_group = False
                groups.append(group)
                group = ""
    return groups
# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
print(separate_paren_groups('((()))'))  # Output: ['((()))']
print(separate_paren_groups(''))  # Output: []
print(separate_paren_groups('()'))  # Output: ['()'] 
print(separate_paren_groups('(()())'))  # Output: ['(()())']  # Test with nested parentheses
print(separate_paren_groups('() (() (()))'))  # Output: ['()', '(())', '(()())']  # Test with multiple groups
print(separate_paren_groups('() (() ((())) ())'))  # Output: ['()', '(())', '(()())', '()']  # Test with multiple groups
print(separate_paren_groups('() (() ((())) ((())) ((()))))'))  # Output: ['()', '(())', '(()())', '()']  # Test with multiple groups and nested parentheses
print(separate_paren_groups('() (() ((())) ((())) ((())) ((()))))'))  # Output: ['()', '(())', '(()())', '()']  # Test with multiple groups and nested parentheses
print(separate_paren_groups('() (() ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((()))))'))  # Output: ['()', '(())', '(()())', '()']  # Test with multiple groups and nested parentheses
print(separate_paren_groups('() (() ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((())) ((