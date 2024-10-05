    def collision(n: int) -> int:
        if n % 2 == 0:
            return n // 2
        else:
            return (n + 1) // 2

    return collision(n)


