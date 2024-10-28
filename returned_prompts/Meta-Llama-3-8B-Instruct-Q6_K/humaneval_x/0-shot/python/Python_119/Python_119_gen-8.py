    def match_parens(lst):
        stack = []
        for s in lst:
            for c in s:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        return 'No'
                    stack.pop()
        return 'Yes' if not stack else 'No'  # Check if stack is empty
    # Test cases
    print(match_parens(['()(', ')']))  # Output: Yes
    print(match_parens([')', ')']))  # Output: No
    print(match_parens(['(', '(']))  # Output: Yes
    print(match_parens(['((', ')']))  # Output: Yes
    print(match_parens([')', '(']))  # Output: No
    print(match_parens(['(', ')']))  # Output: No
    print(match_parens(['(', '']))  # Output: No
    print(match_parens(['', ')']))  # Output: No
    print(match_parens(['(', ')(', ')']))  # Output: Yes
    print(match_parens(['(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', ')']))  # Output: No
    print(match_parens(['(', ')(', ')(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', ')(', ')']))  # Output: No
    print(match_parens(['(', ')(', ')(', ')(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')']))  # Output: No
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')(', ')']))  # Output: No
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')(', ')(', '(']))  # Output: Yes
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')(', ')(', ')']))  # Output: No
    print(match_parens(['(', ')(', ')(', ')(', ')(', ')(', ')(', ')(', '(']))  #