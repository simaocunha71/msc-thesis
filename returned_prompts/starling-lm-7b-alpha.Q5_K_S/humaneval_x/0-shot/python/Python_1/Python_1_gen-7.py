    def _separate_paren_groups(paren_string: str) -> List[str]:
        """Helper function that separates the groups of balanced parentheses.
        """
        stack = []
        for char in paren_string:
            if char in ('(', '['):
                stack.append(char)
            elif char in (')', ']'):
                if stack and char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
        if stack:
            return None
        return ''.join(stack).split('(')

    result = _separate_paren_groups(paren_string)
    if result is None:
        return []
    return result


# Testing the function
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('') == []
    assert separate_paren_groups('( )') == ['']
    assert separate_paren_groups('( ) (( ))') == ['()', '(())']
    assert separate_paren_groups('( ) (( )) ( )') == ['()', '(())', '']


test_separate_paren_groups()


# Main entry point
if __name__ == "__main__":
    result = separate_paren_groups(input())
    print(result)






















































































































