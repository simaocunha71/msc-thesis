    def match_parens(lst):
        stack = []
        for parenthesis in lst[0] + lst[1]:
            if parenthesis == '(':
                stack.append(parenthesis)
            elif parenthesis == ')':
                if stack:
                    stack.pop()
                else:
                    return 'No'
        if stack:
            return 'No'
        return 'Yes'  # if stack is empty, parentheses are balanced
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', ')']))  # 'Yes'  # Balanced
    print(match_parens(['(', '(']))  # 'No'  # Not balanced
    print(match_parens(['', ']']))  # 'No'  # Not valid input
    print(match_parens(['(', ')(', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', '(', ')', ')']))  # 'Yes'  # Balanced
    print(match_parens(['(', ')', '(', ')']))  # 'Yes'  # Balanced
    print(match_parens(['(', ')', ')', '(']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', ')', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', '(']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', '(', ')']))  # 'Yes'  # Balanced
    print(match_parens(['(', ')', '(', ')', '(', ')', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', '(', ')', '(']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', '(', ')', ')', '(']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')', '(', ')', ')', ')']))  # 'No'  # Not balanced
    print(match_parens(['(', ')', '(', ')