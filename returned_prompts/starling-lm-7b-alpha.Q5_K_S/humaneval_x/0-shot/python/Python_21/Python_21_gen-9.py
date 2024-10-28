    min_val = min(numbers)
    max_val = max(numbers)
    scaled_numbers = [(x-min_val)/(max_val-min_val) for x in numbers]
    return scaled_numbers





def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    scaled_numbers = [(x-min_val)/(max_val-min_val) for x in numbers]
    return scaled_numbers




# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]





# 解答




def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    min_val = min(numbers)
    max_val = max(numbers)
    scaled_numbers = [(x-min_val)/(