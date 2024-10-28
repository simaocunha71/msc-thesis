
def is_simple_power(x, n):
    if x<0 or n<0:
        return False
    if x==0 and n==0:
        return False
    if x==1 and n==1:
        return True
    if x==n and n>1:
        return True
    return False
