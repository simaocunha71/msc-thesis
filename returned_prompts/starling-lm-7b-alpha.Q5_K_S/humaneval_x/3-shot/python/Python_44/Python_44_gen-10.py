    def convert_to_base(num: int, base: int):
        result = []
        while num > 0:
            result.append(str(num % base))
            num //= base
        return ''.join(result[::-1])

    if x < base:
        return str(x)
    return convert_to_base(x, base)


