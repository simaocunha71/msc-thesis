def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    s = s1 + s2
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return 'No'
    return 'Yes' if not stack else 'No'  # if stack is empty, the string is good
match_parens(['()(', ')'])  # 'Yes'
match_parens([')', ')'])  # 'No'  # the string is not good because there is no matching '(' for the ')'
match_parens(['(', ')'])  # 'No'  # the string is not good because the stack is not empty at the end, so there is no matching '(' for the ')'
match_parens(['(()', ')'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['((', ')'])  # 'No'  # the string is not good because there is no matching ')' for the '('
match_parens(['(())', '())'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['(())', '())('])  # 'No'  # the string is not good because there is no matching ')' for the '('
match_parens(['((', '())'])  # 'No'  # the string is not good because there is no matching ')' for the '('
match_parens(['(())', '(())'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['()', '(())'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['((', '()'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['(())', '()'])  # 'Yes'  # the string is good, all parentheses are balanced
match_parens(['(())', '())('])  # 'No'  # the string is not good because there is no matching ')' for the '('
match_parens(['((', '())('])  # 'No'  # the string is not good because there is no matching ')' for the '('
match_pare