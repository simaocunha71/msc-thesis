
def make_a_pile(n):
    res = []
    for i in range(n):
        res.append(n)
        n = (n+1)//2 if n%2 else (n+1)//2 * 2
    return res
