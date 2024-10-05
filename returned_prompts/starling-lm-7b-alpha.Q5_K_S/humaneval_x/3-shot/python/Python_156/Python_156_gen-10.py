    def helper(num, symbols):
        result = []
        while num > 0:
            for symbol, value in symbols:
                if num >= value:
                    result.append(symbol)
                    num -= value
                    break
        return ''.join(result)

    symbols = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'),
               (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]

    return helper(number, symbols)


