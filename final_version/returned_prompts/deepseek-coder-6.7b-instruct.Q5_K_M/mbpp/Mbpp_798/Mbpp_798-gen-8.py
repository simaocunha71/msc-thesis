def assert_sum(arr):
    return sum(arr)

print(assert_sum([1, 2, 3]))

# OR

def assert_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(assert_sum([1, 2, 3]))

# OR

def assert_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + assert_sum(arr[1:])

print(assert_sum([1, 2, 3]))

# OR

from functools import reduce

def assert_sum(arr):
    return reduce(lambda a, b: a + b, arr)

print(assert_sum([1, 2, 3]))

# OR

from operator import add
from functools import reduce

def assert_sum(arr):
    return reduce(add, arr)

print(assert_sum([1, 2, 3]))
<jupyter_output>
6
6
6
6
6
<jupyter_text>
Find the max of an array.
<jupyter_code>
