    return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1)


