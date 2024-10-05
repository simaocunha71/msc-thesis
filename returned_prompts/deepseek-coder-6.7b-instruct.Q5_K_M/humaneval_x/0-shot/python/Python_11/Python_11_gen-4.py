from typing import List

def string_tuple(*args: str) -> str:
    return ', '.join(args)

print(string_tuple('010', '110'))
print(string_tuple('100', '111'))
print(string_tuple('000', '010', '100', '111