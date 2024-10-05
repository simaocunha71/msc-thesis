
def will_it_fly(q,w):
    if sum(q) > w:
        return False
    elif sum(q) == w:
        return True
    else:
        return True if q == q[::-1] and sum(q) <= w else False
