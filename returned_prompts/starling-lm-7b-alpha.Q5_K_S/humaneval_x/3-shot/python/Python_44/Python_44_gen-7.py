    def convert_to_base(x, base):
        if x < 0:
            return '-' + convert_to_base(-x, base)
        digits = []
        while x:
            digits.append(str(x % base))
            x //= base
        return ''.join(digits[::-1])

    return convert_to_base(x, base)


