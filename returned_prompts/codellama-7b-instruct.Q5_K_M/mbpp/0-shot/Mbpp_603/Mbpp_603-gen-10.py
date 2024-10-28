def get_lucid(n):
    """
    :param n: int
    :return: list[int]
    """
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            if i % 4 == 0:
                result.append(i)
        else:
            if i % 4 != 0:
                result.append(i)
    return result

# def get_ludic(n):
#     """
#     :param n: int
#     :return: list[int]
#     """
#     return [i for i in range(1, n+1) if i % 2 == 0 or i % 4 != 0]
