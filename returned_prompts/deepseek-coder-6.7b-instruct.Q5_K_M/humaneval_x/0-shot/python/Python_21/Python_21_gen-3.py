from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

This will give you the output:
[0.0, 0.25, 0.5, 0.75, 1.0]

This is because it first finds the minimum and maximum of the numbers in the list, and then it applies a linear transformation to each number in the list. This transformation scales the numbers so that the minimum becomes 0 and the maximum becomes 1.
"""

import doctest
doctest.run_docstring_examples(rescale_to_unit, globals())

# The output should be:
# >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
# [0.0, 0.25, 0.5, 0.75, 1.0]
# >>> 
# 0 tests passed.
# 0 failed tests.
# 0 tests omitted.
# 1 passed and 0 failed. Test passed.
<jupyter_output>
0 tests passed.
0 failed tests.
0 tests omitted.
1 passed and 0 failed. Test passed.
<jupyter_text>
Exercise 2: Create a function to calculate the mean and standard deviation
<jupyter_code>
"""
