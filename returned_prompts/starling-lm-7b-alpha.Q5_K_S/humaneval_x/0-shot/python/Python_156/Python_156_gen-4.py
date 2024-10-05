    from typing import Tuple
    symbols = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i")
    ]

    def int_to_mini_roman(number: int) -> str:
        result = ""
        for count, symbol in symbols:
            result += symbol * (number // count)
            number %= count
        return result

# Test Cases:
print(int_to_mini_roman(19) == 'xix')
print(int_to_mini_roman(152) == 'clii')
print(int_to_mini_roman(426) == 'cdxxvi')







```
