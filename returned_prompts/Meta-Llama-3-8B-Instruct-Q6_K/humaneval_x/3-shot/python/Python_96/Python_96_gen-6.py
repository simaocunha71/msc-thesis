    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_up_to(n: int) -> List[int]:
        result = []
        for i in range(2, n):
            if is_prime(i):
                result.append(i)
        return result


