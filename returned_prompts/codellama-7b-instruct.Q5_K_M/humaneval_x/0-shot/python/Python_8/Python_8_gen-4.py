def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    :param numbers: list of integers
    :return: tuple of sum and product
    """
    return sum(numbers), reduce(lambda x, y: x * y, numbers, 1)