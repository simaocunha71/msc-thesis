
    def make_a_pile(n):
        pile = []
        if n % 2 == 0:
            for i in range(n):
                pile.append(n + 2*i)
        else:
            for i in range(n):
                pile.append(n + 2*i)
        return pile

    print(make_a_pile(3))

    """
    def make_a_pile(n):
        return [n + 2*i for i in range(n)]
    """

"""
def make_a_pile(n):
    return [n + 2*i for i in range(n)]

print(make_a_pile(3))
"""
"""
def make_a_pile(n):
    return [n + 2*i if n % 2 == 0 else n + 2*i for i in range(n)]
"""
"""
def make_a_pile(n):
    return [n + 2*i if i % 2 == 0 else n + 2*i + 1 for i in range(n)]
"""
"""
def make_a_pile(n):
    return [n + 2*i if n % 2 == i % 2 else n + 2*i + 1 for i in range(n)]
"""
"""
def make_a_pile(n):
    return [n + 2*i if n % 2 == 0 else n + 2*i + 1 for i in range(n)]
"""
"""
def make_a_pile(n):
    return [n + 2*i if n % 2 == 0 else n + 2*i for i in range(n)]
"""
"""
def make_a_pile(n):
    return [n + 2*i for i in range(n)]
"""

# 2022-02-13 19:57:06

# 2022-02-13 19:57:56

# 2022-02-13 19:58:13

# 2022-02-