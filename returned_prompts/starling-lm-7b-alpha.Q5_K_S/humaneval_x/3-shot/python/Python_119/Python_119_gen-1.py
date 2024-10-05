    def check(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False

        return count == 0

    return 'Yes' if check(lst[0]) or check(lst[1]) or check(''.join(lst)) else 'No'


