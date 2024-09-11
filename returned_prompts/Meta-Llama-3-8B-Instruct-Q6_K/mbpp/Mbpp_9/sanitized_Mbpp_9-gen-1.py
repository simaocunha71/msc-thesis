def find_Rotations(s: str) -> int:
    return len(s) // gcd(len(s), 1)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a