def get_ludic(n: int) -> list:
    def is_ludic(num: int) -> bool:
        return math.sqrt(num).is_integer()

    return [i for i in range(1, n+1) if is_ludic(i)]

