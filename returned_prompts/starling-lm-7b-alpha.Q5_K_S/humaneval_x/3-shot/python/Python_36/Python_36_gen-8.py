    def helper(n: int):
        result = 0
        for i in range(11, n + 1, 11):
            if i % 7 == 0:
                result += 1
        for i in range(13, n + 1, 13):
            if i % 7 == 0:
                result += 1
        return result

    return helper(n)


