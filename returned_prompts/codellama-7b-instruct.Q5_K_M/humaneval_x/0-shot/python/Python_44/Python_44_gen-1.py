
def change_base(x: int, base: int):
    return bin(x)[2:].zfill(base).replace('1', '1').replace('0', '2')


