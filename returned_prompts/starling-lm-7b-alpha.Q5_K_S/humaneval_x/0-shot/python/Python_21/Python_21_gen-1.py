def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(x - min_num) / (max_num - min_num) for x in numbers]




    # Given list of numbers (of at least two elements), apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    # >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    # [0.0, 0.25, 0.5, 0.75, 1.0]


    # First, find the minimum and maximum in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Then, subtract the minimum from each element in the list
    # This will ensure that the smallest number in the list is now 0
    numbers = [x - min_num for x in numbers]

    # Next, divide each element in the list by the difference between the maximum and minimum
    # This will ensure that the largest number in the list is now 1
    numbers = [x / (max_num - min_num) for x in numbers]

    # Finally, return the transformed list
    return numbers




def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # First, find the minimum and maximum in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Then, subtract the minimum