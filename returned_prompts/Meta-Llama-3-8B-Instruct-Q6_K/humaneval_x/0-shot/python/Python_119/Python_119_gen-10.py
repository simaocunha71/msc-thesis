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
        return 'Yes'
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'







# Python code for stack implementation
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
    return 'Yes'
# Driver code
if __name__ == "__main__":
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'





# Python code for stack implementation
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
    return 'Yes'
# Driver code
if __name__ == "__main__":
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'





# Python code for stack implementation
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
    return 'Yes'
# Driver code
if __name__ == "__main__":
    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens