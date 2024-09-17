```
import math
def multiply_num(nums):
    product = 1
    for num in nums:
        product *= num
    return product / len(nums)
```



The function `multiply_num` takes a list of numbers as input, multiplies all the numbers together, and then divides the result by the length of the list. The result is then returned.

The unit test provided, `assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)`, ensures that the function is working correctly by comparing the result with the expected output. The `math.isclose` function is used to compare the result with the expected output, allowing for a small tolerance in the comparison. This is necessary because floating point calculations can sometimes result in small errors. The `rel_tol=0.001` argument specifies that the comparison should be done with a relative tolerance of 0.001, meaning that the actual result can be up to 0.001% different from the expected result and still be considered correct.