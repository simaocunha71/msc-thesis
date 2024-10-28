    sum_product_sum = 0
    sum_product_product = 1
    for i in range(len(numbers)):
        sum_product_sum += numbers[i]
        sum_product_product *= numbers[i]
    return (sum_product_sum, sum_product_product)


def sum_product_list(numbers: List[int]) -> List[Tuple[int, int]]:
    """For a given list of integers, return a list of tuples, where each tuple contains a sum and a product of contiguous sub-segments of the list. The first tuple should be a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product_list([])
    [(0, 1), ]
    >>> sum_product_list([1, 2, 3, 4])
    [(10, 24), (10, 24), (10, 24), (10, 24)]
    """

    sum_product_list = [(sum(numbers), reduce(lambda x, y: x * y, numbers))]
    for i in range(len(numbers)-1):
        sum_product_list.append((sum_product_list[i][0] + numbers[i+1], sum_product_list[i][1] * numbers[i+1]))
    return sum_product_list


def sum_product_2d_list(numbers: List[int]) -> List[List[int]]:
    """For a given list of integers, return a 2D list where each row contains a sum and a product of contiguous sub-segments of the list. The first row should be a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product_2d_list([])
    [[0, 1], ]
    >>> sum_product_2d_list([1, 2, 3, 4])
   