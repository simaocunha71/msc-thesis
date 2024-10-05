    def is_good(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                if count == 0:
                    return False
                count -= 1
        return count == 0

    return 'Yes' if is_good(lst[0] + lst[1]) else 'No'


