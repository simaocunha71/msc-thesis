def find_Rotations(s):
    return len(s) // gcd(len(s), len(s))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a