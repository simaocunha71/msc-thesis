    def match_parens(lst):
        stack = []
        for s in lst:
            for c in s:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if stack:
                        stack.pop()
                    else:
                        return 'No'
        return 'Yes' if not stack else 'No'
    # test cases
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'
    print(match_parens(['(()', ')']))  # 'Yes'
    print(match_parens([')', '(']))  # 'No'
    print(match_parens(['((', ')(']))  # 'Yes'
    print(match_parens(['))', '(']))  # 'No'














Solutions

Solution 1:
```
def match_parens(lst):
    stack = []
    for s in lst:
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    return 'No'
    return 'Yes' if not stack else 'No'
```
Solution 2:
```
def match_parens(lst):
    count_open = 0
    count_close = 0
    for s in lst:
        for c in s:
            if c == '(':
                count_open += 1
            elif c == ')':
                count_close += 1
    return 'Yes' if count_open == count_close else 'No'
```
Solution 3:
```
def match_parens(lst):
    count_open = 0
    count_close = 0
    for s in lst:
        for c in s:
            if c == '(':
                count_open += 1
            elif c == ')':
                count_close += 1
        if count_open > count_close:
            return 'No'
    return 'Yes'
```





Explanation:
The problem is asking to check if it's possible to concatenate the two strings in some order, that the resulting string will be good. A string S is considered to be good if and only if all parentheses in S are balanced. For example: the string '(())()' is good, while the string '())' is not.

The solution can be achieved by using a stack to keep track of the opening parentheses. When a closing parenthesis is encountered, we check if