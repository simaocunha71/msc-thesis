
def make_a_pile(n):
    # write your solution here
    return [n] + [x for x in range(n+1, 0, -2) if x % 2 != 0]
