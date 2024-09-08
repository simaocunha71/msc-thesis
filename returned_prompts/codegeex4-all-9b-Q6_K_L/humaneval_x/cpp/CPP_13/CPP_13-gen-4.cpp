def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def gcd(a,b):
    if a==0:
        return b
    return gcd(b,a%b)
def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
