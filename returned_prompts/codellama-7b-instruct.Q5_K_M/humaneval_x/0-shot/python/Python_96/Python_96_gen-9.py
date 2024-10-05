
def count_up_to(n):
    if n < 2: return []
    return [x for x in range(2, n+1) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0]
