    sum_product_tuple = (sum(numbers), 1)
    for num in numbers:
        sum_product_tuple = (sum_product_tuple[0] + num, sum_product_tuple[1] * num)
    return sum_product_tuple


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("*** Test Passed.")
    else:
        print("*** Test Failed.")





```

# Solution:
# The idea is to create a tuple which will consist of sum and product of all the integers. If the list is empty, the sum should be equal to 0 and the product should be equal to 1.
# The function "sum_product" takes the list of integers as input and returns a tuple. In the beginning, initialize the tuple as (sum(numbers), 1). Then, iterate through the numbers in the list and update the tuple as follows: (sum_product_tuple[0] + num, sum_product_tuple[1] * num). Finally, return the tuple.
# To test the function, use the assertions provided in the code. The "doctest" module is used to test the function and check if the test cases are passed or failed. If all the test cases are passed, print "*** Test Passed." Otherwise, print "*** Test Failed."

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_product_tuple = (sum(numbers), 1)
    for num in numbers:
        sum_product_tuple = (sum_product_tuple[0] + num, sum_product_tuple[1] * num)
    return sum_product_tuple
```

To test the function, you can call it with an empty list and a list of integers:

```python
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  #