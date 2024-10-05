    def is_balanced(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    for first in lst:
        for second in lst:
            if first != second:
                if is_balanced(first + second) or is_balanced(second + first):
                    return 'Yes'
    return 'No'

