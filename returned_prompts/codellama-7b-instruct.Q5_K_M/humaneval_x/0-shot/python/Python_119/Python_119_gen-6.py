
    def match_parens(lst):
        stack = []
        for item in lst:
            if item == '(':
                stack.append(item)
            else:
                if len(stack) == 0:
                    return 'No'
                stack.pop()
        if len(stack) == 0:
            return 'Yes'
        else:
            return 'No'

    if __name__ == '__main__':
        print(match_parens(['()(', ')']))
        print(match_parens(['()', ')']))
        print(match_parens(['()()()', ')']))
        print(match_parens(['()()()', '()']))
        print(match_parens(['())(((', ')', '(']))
        print(match_parens(['()(', '()']))
        print(match_parens([')', '(']))
        print(match_parens(['()()', '()']))
        print(match_parens(['()', '()()']))
        print(match_parens(['()', '()()'])
        print(match_parens(['()()', '()()']))
