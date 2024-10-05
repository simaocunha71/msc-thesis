    from collections import defaultdict

    # Build a mapping from integer values to Roman symbols.
    mapping = defaultdict(str)
    mapping[1000] = 'm'
    mapping[900] = 'cm'
    mapping[500] = 'd'
    mapping[400] = 'cd'
    mapping[100] = 'c'
    mapping[90] = 'xc'
    mapping[50] = 'l'
    mapping[40] = 'xl'
    mapping[10] = 'x'
    mapping[9] = 'ix'
    mapping[5] = 'v'
    mapping[4] = 'iv'
    mapping[1] = 'i'

    # Return the Roman representation of a given integer.
    def roman(n):
        res = ''
        while n > 0:
            for key, symbol in mapping.items():
                while n >= key:
                    res += symbol
                    n -= key
        return res

    return roman(number)



# Made by: Tiancheng ZHANG (zhangtiancheng0217@gmail.com)
# Date: 2018-01-08
# License: MIT License
















































































































































































































