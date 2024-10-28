def get_ludic(n):
    def is_ludic(num):
        digits = set(str(num))
        return len(digits) == len(str(num))

    return [i for i in range(1, n+1) if is_ludic(i)]