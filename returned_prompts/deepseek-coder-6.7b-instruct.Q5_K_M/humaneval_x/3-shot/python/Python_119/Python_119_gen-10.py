    def is_valid(s):
        stack = []
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    s1, s2 = lst
    return 'Yes' if (is_valid(s1 + s2) or is_valid(s2 + s1)) else 'No'


