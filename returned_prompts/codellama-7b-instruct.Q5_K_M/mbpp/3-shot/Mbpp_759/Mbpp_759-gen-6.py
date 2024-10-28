
def is_decimal(n: str):
    return n.replace('.', '').isdigit() and float(n) % 1 == 0


