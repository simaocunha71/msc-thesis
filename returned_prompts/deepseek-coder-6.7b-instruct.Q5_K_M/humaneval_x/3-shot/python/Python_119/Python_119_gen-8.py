    def is_good(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0

    return 'Yes' if is_good(lst[0] + lst[1]) else 'No'


