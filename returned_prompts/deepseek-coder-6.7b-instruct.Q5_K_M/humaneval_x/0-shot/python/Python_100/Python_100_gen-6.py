
def make_a_pile(n):
    levels = [n]
    for i in range(n-1):
        if n % 2 == 0:
            n += 2
        else:
            n += 2
        levels.append(n)
    return levels

print(make_a_pile(3))


