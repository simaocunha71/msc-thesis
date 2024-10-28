    def factorize_helper(n: int, factor: int = 2) -> List[int]:
        if factor * factor > n:
            if n > 1:
                return [n]
            return []

        count = 0
        while n % factor == 0:
            n //= factor
            count += 1

        if count > 0:
            return [count] + factorize_helper(n, factor + 1)

        return factorize_helper(n, factor + 1)

    return factorize_helper(n)


