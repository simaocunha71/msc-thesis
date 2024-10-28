from math import sqrt
def prime_num(x):
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    if x==3:
        return True
    if x%3==0:
        return False
    d=5
    while d<=sqrt(x):
        if x%d==0:
            return False
        if x%(d+2)==0:
            return False
        d+=6
    return True