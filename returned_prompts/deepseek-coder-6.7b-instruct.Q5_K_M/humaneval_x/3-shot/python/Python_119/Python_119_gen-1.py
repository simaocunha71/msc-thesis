    s1, s2 = lst
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

    for perm in permutations(lst):
        if is_good(perm[0] + perm[1]):
            return 'Yes'
    return 'No'


