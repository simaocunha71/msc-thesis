
def change_base(x: int, base: int):
    return bin(x)[2:][::-1].replace('0', str(base))
