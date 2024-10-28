
def will_it_fly(q,w):
    if sum(q) > w:
        return False
    elif q == q[::-1]:
        return True
    else:
        return False
