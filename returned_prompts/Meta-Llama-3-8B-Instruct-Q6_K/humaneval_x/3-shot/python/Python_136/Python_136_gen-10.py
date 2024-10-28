    largest_negative = None
    smallest_positive = None

    for num in lst:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num

    return largest_negative, smallest_positive
# or
def largest_smallest_integers(lst):
    largest_negative = max([num for num in lst if num < 0], default=None)
    smallest_positive = min([num for num in lst if num > 0], default=None)
    return largest_negative, smallest_positive
# or
def largest_smallest_integers(lst):
    largest_negative = max((num for num in lst if num < 0), default=None)
    smallest_positive = min((num for num in lst if num > 0), default=None)
    return largest_negative, smallest_positive
# or
def largest_smallest_integers(lst):
    result = (None, None)
    for num in lst:
        if num < 0 and (result[0] is None or num > result[0]):
            result = (num, result[1])
        elif num > 0 and (result[1] is None or num < result[1]):
            result = (result[0], num)
    return result
# or
def largest_smallest_integers(lst):
    result = [None, None]
    for num in lst:
        if num < 0 and result[0] is None or num > result[0]:
            result[0] = num
        elif num > 0 and result[1] is None or num < result[1]:
            result[1] = num
    return result
# or
def largest_smallest_integers(lst):
    return max((num for num in lst if num < 0), default=None), min((num for num in lst if num > 0), default=None)
# or
def largest_smallest_integers(lst):
    result = []
    for num in lst:
        if num < 0:
            result.append(num)
        elif num > 0:
            result.append(num)
    if not result:
        return None, None
    return max(result, default=None), min(result, default=None)
# or
def largest_smallest_integers(lst):
    max_negative = max((num for num in lst if num < 0