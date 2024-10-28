    def mini_roman(n):
        m = {
            1000: 'm',
            900: 'cm',
            500: 'd',
            400: 'cd',
            100: 'c',
            90: 'xc',
            50: 'l',
            40: 'xl',
            10: 'x',
            9: 'ix',
            5: 'v',
            4: 'iv',
            1: 'i'
        }
        result = []
        for k, v in m.items():
            while n >= k:
                result.append(v)
                n -= k
        return ''.join(result)
    return mini_roman(number)


