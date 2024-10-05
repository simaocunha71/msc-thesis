
def x_or_y(n, x, y):
    if n%2==0:
        return y
    else:
        return x

#or

def x_or_y(n, x, y):
    return x if n%2==0 else y

#or

def x_or_y(n, x, y):
    return y if n%2==0 else x