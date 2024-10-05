
    def match_parens(lst):
        s1, s2 = lst
        for c in s1 + s2:
            if c == '(':
                s1 += c
            else:
                if not s1:
                    s2 = c + s2
                else:
                    s1 = s1[:-1]
        return 'Yes' if not s1 else 'No'

    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'

The function works by iterating over each character in the strings, and adding any open parentheses to s1, and any close parentheses to s2. If a close parenthesis is encountered and s1 is empty, it means that this close parenthesis is not enclosed in an open parenthesis, so it is moved to the beginning of s2. If a close parenthesis is encountered and s1 is not empty, it means that this close parenthesis is enclosed in the last open parenthesis, so the last open parenthesis is removed from s1. If the strings have been iterated over and s1 is empty, it means that all parentheses are balanced, so 'Yes' is returned. If s1 is not empty, it means that there are unbalanced parentheses, so 'No' is returned.

The time complexity of this function is O(n), where n is the total number of characters in the strings. This is because the function iterates over each character in the strings once. The space complexity is O(n), where n is the total number of characters in the strings. This is because the function uses additional space to store the strings s1 and s2.
    '''

    return solution


def test_match_parens():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
    assert match_parens(['(', ')']) == 'Yes'
    assert match_parens(['(', '(']) == 'No'
    assert match_parens(['((', ')(']) == 'No'
    assert match_parens(['((', '))']) ==