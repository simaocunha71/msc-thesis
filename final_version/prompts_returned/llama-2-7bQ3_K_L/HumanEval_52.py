

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return sum(x < t for x in l) == len(l)


def solution():
    file = open("input.txt", "r")
    
    lines = [line for line in file]
    n, l, r = map(int, lines[0].split())
    c = [x for x in lines[1][-2:] if (len(x) != 1 or int(x[-1]) == 0)]
    
    l1, l2 = map(int, lines[3:6])

    m1 = map(int, lines[7:])
    m2 = [x for x in range(len(l)) if (x not in c) and (x < 50)]
    
    print("Case #{}: {}".format(case + 1, below_threshold([*m1, l[n - 1]], r)))
