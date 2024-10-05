from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ''
    for char in paren_string:
        if char == '(':
            current_group += char
        elif char == ')':
            current_group += char
            if current_group.count('(') == current_group.count(')'):
                result.append(current_group)
                current_group = ''
    return result
# test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
# ['()', '(())', '(()())']



# test cases
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'], f"Expected ['()', '(())', '(()())'] but got {separate_paren_groups('( ) (( )) (( )( ))')}"
assert separate_paren_groups('') == [], f"Expected an empty list but got {separate_paren_groups('')}"
assert separate_paren_groups('(') == ['('], f"Expected ['('] but got {separate_paren_groups('(')}" 
assert separate_paren_groups(')') == [')'], f"Expected [')'] but got {separate_paren_groups(')')}"
assert separate_paren_groups('((()))') == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))')}"
assert separate_paren_groups(')(') == [], f"Expected an empty list but got {separate_paren_groups(')(')}"
assert separate_paren_groups('((()))(') == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))(')}"
assert separate_paren_groups('((()))')) == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))')}"
assert separate_paren_groups('((()))((') == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))((')}"
assert separate_paren_groups('((()))')) == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))')}"
assert separate_paren_groups('((()))((') == ['((()))'], f"Expected ['((()))'] but got {separate_paren_groups('((()))((')}"
assert separate_paren_groups('((()))') == ['((()))'], f"Expected