    apples, oranges = map(int, s.split('apples and')[0].split() + s.split('apples and')[1].split()[:1])
    return n - apples - oranges

