
def is_woodall(n):
    d = {
        "0": False,
        "1": False,
        "2": False,
        "3": True,
        "4": False,
        "5": False,
        "6": False,
        "7": False,
        "8": False,
        "9": False
    }
    while n > 0:
        if d[str(n % 10)]:
            return False
        n //= 10
    return True


