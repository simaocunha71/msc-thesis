    def match_parens(lst):
        s1 = lst[0]
        s2 = lst[1]
        stack = []
        for char in s1 + s2:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return 'No'
        if stack:
            return 'No'
        return 'Yes'  # if stack is empty, the string is good


    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'
    print(match_parens(['(', ')']))  # 'Yes'
    print(match_parens(['))', '(']))  # 'No'
    print(match_parens(['(', '(']))  # 'Yes'
    print(match_parens(['', '(']))  # 'No'
    print(match_parens(['(', '']))  # 'Yes'
    print(match_parens(['(' , '(']))  # 'Yes'
    print(match_parens([')(', '(']))  # 'No'
    print(match_parens(['(', ')(', '(']))  # 'Yes'
    print(match_parens([')(', '(' , '(']))  # 'No'
    print(match_parens(['(', '(', '(']))  # 'Yes'  # 
    print(match_parens([')(', ')(', '(']))  # 'No'
    print(match_parens(['(', ')(', '(' , '(']))  # 'Yes'
    print(match_parens([')(', ')(', '(' , '(' , '(']))  # 'No'
    print(match_parens(['(', ')(', '(' , '(' , '(' , '(']))  # 'Yes'
    print(match_parens([')(', ')(', '(' , '(' , '(' , '(' , '(']))  # 'No'
    print(match_parens(['(', ')(', '(' , '(' , '(' , '(' , '(' , '(']))  # 'Yes'
    print(match_parens([')(', ')(', '(' , '(' , '(' , '(' , '(' , '(' , '(']))  # 'No'
    print(match_parens(['(', ')(', '(' , '(' , '(' , '(' , '(' , '(' , '(' , '(']))  # 'Yes'
    print(match_parens([')(', ')(', '(' , '(' , '(' , '(' , '(' , '(' , '(' ,