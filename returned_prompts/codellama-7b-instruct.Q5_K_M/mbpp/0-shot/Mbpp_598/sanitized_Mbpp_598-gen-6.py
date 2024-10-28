def armstrong_number(n):
    x=n
    y=0
    while x>0:
        y+=x%10
        x//=10
    return y==n