    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    # Alternative solution:
    # if n < 2:
    #     return False
    # for i in range(2, int(n**0.5) + 1):
    #     if n % i == 0:
    #         return False
    # return n > 1
    # or
    # return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)) and n % n == 0


