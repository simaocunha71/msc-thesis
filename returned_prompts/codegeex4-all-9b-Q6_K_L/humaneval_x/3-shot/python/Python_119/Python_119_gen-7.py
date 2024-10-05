    def count_parentheses(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    if count_parentheses(lst[0] + lst[1]) == 0:
        return 'Yes'
    else:
        return 'No'