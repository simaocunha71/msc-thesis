def get_ludic(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    ludics = []
    for i in range(1, n+1):
        if is_prime(i) or any(is_prime(j) and is_prime(i-j) for j in range(2, i)):
            ludics.append(i)
    return ludics