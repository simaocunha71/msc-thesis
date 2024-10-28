def get_ludic(n):
    def is_ludic(num):
        digits = list(str(num))
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if digits[i] == digits[j]:
                    return False
        return True

    return [i for i in range(1, n + 1) if is_ludic(i)]