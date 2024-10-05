    def convert_to_base(number: int, base: int) -> str:
        if number < base:
            return str(number)
        else:
            return convert_to_base(number // base, base) + str(number % base)

    return convert_to_base(x, base)


