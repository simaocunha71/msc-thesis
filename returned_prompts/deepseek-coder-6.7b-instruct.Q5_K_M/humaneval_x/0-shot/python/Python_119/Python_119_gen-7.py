
    def match_parens(lst):
        s1, s2 = lst
        if s1.count('(') < s1.count(')') or s2.count('(') < s2.count(')'):
            return 'No'
        if s1.count(')') > s2.count('('):
            return 'No'
        if s1.count('(') - s1.count(')') > s2.count('(') - s2.count(')'):
            return 'No'
        return 'Yes'

    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'
    print(match_parens(['(', ')']))  # 'Yes'
    print(match_parens(['(', '(']))  # 'No'
    print(match_parens(['(', ')(']))  # 'Yes'
    print(match_parens([')(', ')']))  # 'No'
    print(match_parens(['()', ')']))  # 'No'
    print(match_parens(['(', '())']))  # 'Yes'
    print(match_parens(['(', '()']))  # 'No'
    print(match_parens([')', '()']))  # 'No'
    print(match_parens(['(', ')(']))  # 'Yes'
    print(match_parens([')(', ')']))  # 'No'
    print(match_parens(['()', ')']))  # 'No'
    print(match_parens(['(', '())']))  # 'Yes'
    print(match_parens(['(', '()']))  # 'No'
    print(match_parens([')', '()']))  # 'No'
    print(match_parens(['(', ')(']))  # 'Yes'
    print(match_parens([')(', ')']))  # 'No'
    print(match_parens(['()', ')']))  #