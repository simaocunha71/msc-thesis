
def make_a_pile(n):
    pile = []
    while n > 0:
        pile.append(n)
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        n -= 1
    return pile

# Alternative implementation using recursion
def make_a_pile(n):
    if n == 0:
        return []
    elif n % 2 == 0:
        pile = make_a_pile(n-2)
        pile.append(n)
    else:
        pile = make_a_pile(n-1)
        pile.append(n)
    return pile


make_a_pile(3)




make_a_pile(6)




make_a_pile(9)




make_a_pile(10)




make_a_pile(11)




make_a_pile(12)




make_a_pile(13)




make_a_pile(14)




make_a_pile(15)




make_a_pile(16)




make_a_pile(17)




make_a_pile(18)




make_a_pile(19)




make_a_pile(20)




make_a_pile(21)




make_a_pile(22)




make_a_pile(23)




make_a_pile(24)




make_a_pile(25)




make_a_pile(26)




make_a_pile(27)




make_a_pile(28)




make_a_pile(29)




make