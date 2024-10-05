from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    s = 0
    p = 1
    for num in numbers:
        s += num
        p *= num
    return (s, p)


print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)


# Alternatively, you can use the built-in `sum` function and `functools.reduce` function from the `functools` module:

from typing import List, Tuple
from functools import reduce


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    s = sum(numbers)
    p = reduce(lambda a, b: a*b, numbers, 1)
    return (s, p)


print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)

# Note: The `reduce` function applies a binary function (in this case, a lambda function that multiplies two numbers) to all items of an iterable (in this case, the list of numbers) in a cumulative way. The optional third argument is the initializer, which is the starting value in the cumulative computation.


# Also note that in Python, it's not considered good practice to use built-in names for your variables. For example, using `list` as a variable name.
<jupyter_output>
<empty_output>
<jupyter_text>
