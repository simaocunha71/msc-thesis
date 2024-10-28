
def make_a_pile(n):
    p = []
    while n > 0:
        p.append(n)
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        n -= 1
    return p

# Tests
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(4))  # [4, 6, 8]
print(make_a_pile(5))  # [5, 7, 9, 11]




def make_a_pile(n):
    pile = [n]
    while n > 0:
        if n % 2:
            n += 1
        else:
            n += 2
        pile.append(n)
        n -= 1
    return pile

# Tests
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(4))  # [4, 6, 8]
print(make_a_pile(5))  # [5, 7, 9, 11]




def make_a_pile(n):
    pile = [n]
    while n > 0:
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        pile.append(n)
        n -= 1
    return pile

# Tests
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(4))  # [4, 6, 8]
print(make_a_pile(5))  # [5, 7, 9, 11]




def make_a_pile(n):
    pile = [n]
    while n > 0:
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        pile.insert(0,