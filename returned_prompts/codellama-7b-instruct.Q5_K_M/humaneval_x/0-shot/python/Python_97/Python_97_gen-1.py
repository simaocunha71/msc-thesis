
def multiply(a, b):
    a = str(abs(a))
    b = str(abs(b))
    return int(a[-1]) * int(b[-1]) if a != '0' and b != '0' else 0
