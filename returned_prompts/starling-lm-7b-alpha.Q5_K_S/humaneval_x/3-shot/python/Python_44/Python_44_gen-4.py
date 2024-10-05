    def helper(x: int, base: int) -> str:
        if x == 0:
            return '0'
        elif x < base:
            return str(x % base) + helper(x // base, base)
        else:
            return helper(x // base, base) + str(x % base)

    return helper(x, base)


