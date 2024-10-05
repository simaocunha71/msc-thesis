from typing import List, Tuple


def sum_product(numbers: List[int]) - Tuple[int, int]:
    
    sum_numbers = 0
    product_numbers = 1
    for number in numbers:
        sum_numbers += number
        product_numbers *= number
    return (sum_numbers, product_numbers)


print(sum_product([]))
print(sum_product([1, 2, 3, 4]))


# Or we can use built-in Python functions sum() and functools.reduce()

from functools import reduce
from operator import mul

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    if not numbers:
        return (0, 1)
    else:
        return (sum(numbers), reduce(mul, numbers))


print(sum_product([]))
print(sum_product([1, 2, 3, 4]))

# Both will give the same output. The first one is more manual and less built-in. The second one is more concise but more built-in.

```

## 11. Write a Python program that takes a string of words separated by commas and returns a list of those words.

