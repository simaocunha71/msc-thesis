    apples, oranges = map(int, s.split()[0::2])
    total_fruits = int(s.split()[-1])
    return total_fruits - apples - oranges


