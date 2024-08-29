def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

B:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

C:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

D:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b % a, a)

E:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    else:
        return gcd(a % b, a)

F:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

G:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

H:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return gcd(a % b, a)

I:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b % a, b)
J:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

K:
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return gcd(a % b