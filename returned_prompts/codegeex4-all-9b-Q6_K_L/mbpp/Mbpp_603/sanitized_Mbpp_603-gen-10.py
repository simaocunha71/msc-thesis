def get_ludic(n):
    def is_ludic(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [i for i in range(1, n + 1) if is_ludic(i)]