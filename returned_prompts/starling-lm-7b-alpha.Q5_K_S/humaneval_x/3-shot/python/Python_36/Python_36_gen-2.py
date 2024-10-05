    def fizz_buzz_helper(n: int) -> int:
        count = 0
        for i in range(n):
            if (i + 1) % 11 == 0 or (i + 1) % 13 == 0:
                if str(i + 1).count('7') > 0:
                    count += 1
        return count

    return fizz_buzz_helper(n)


