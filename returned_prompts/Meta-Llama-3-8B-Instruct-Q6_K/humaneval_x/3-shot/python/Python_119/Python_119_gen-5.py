    stack = []
    for c in lst[0]:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return 'No'
    for c in lst[1]:
        if c == '(':
            if stack:
                stack.pop()
            else:
                return 'No'
        elif c == ')':
            stack.append(c)
    return 'Yes' if not stack else 'No'  # If stack is empty, then all parentheses were matched, so the string is good. Otherwise, it's not.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes' if all parentheses were matched, 'No' otherwise.  # 'Yes'