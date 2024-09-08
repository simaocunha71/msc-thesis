def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[-1]+b[:-1]:
            return True
    return False
B:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b or a[i:i+len(b)] == b[-1]+b[:-1]:
            return True
    return False

C:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b[-1]+b[:-1]:
            return True
        if a[i:i+len(b)] == b:
            return True
    return False
D:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[-1]+b[:-1]:
            return True
    return True
E:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b or a[i:i+len(b)] == b[-1]+b[:-1]:
            return False
    return True
F:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return True
        if a[i:i+len(b)] == b[-1]+b[:-1]:
            return False
    return True

G:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b or a[i:i+len(b)] == b[-1]+b[:-1]:
            return False
    return True
H:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b[-1]+b[:-1]:
            return False
        if a[i:i+len(b)] == b:
            return False
    return True

I:
def cycpattern_check(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b[-1]+b