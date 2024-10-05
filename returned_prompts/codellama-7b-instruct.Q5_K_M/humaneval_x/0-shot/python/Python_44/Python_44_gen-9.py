
def change_base(x: int, base: int):
    return str(bin(x)[2:]) if base == 2 else str(hex(x)[2:]) if base == 16 else str(oct(x)[2:]) if base == 8 else str(x)