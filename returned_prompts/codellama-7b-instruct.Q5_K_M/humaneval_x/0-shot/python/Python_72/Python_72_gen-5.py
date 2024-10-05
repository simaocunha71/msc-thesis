
def will_it_fly(q, w):
    sum = 0
    for i in q:
        sum += i
    if sum > w:
        return False
    elif q == q[::-1]:
        return True
    else:
        return False