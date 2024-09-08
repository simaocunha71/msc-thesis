def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % p
B:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n + 1, p)) % p
C:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return (n * modp(n - 1, p)) % p
D:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % (p - 1)
E:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % (p + 1)
F:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % p + 1
G:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % p - 1
H:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n + 1, p)) % p
I:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return (n * modp(n - 1, p)) % (p + 1)
J:
def modp(n, p):
    if n == 0:
        return 1
    elif n == 1