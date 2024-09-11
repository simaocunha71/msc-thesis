"""
def first_odd(nums):
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            return nums[i]

def test_first_odd():
    assert first_odd([1,3,5]) == 1
    print("All tests passed")

test_first_odd()
"""

def first_odd(nums):
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            return nums[i]
    return None

def test_first_odd():
    assert first_odd([1,3,5]) == 1
    print("All tests passed")

test_first_odd()

```
This function `first_odd` takes in a list of numbers and iterates through each number. If the number is odd (not divisible by 2), the function will return that number. If no odd numbers are found in the list, the function will return `None`.

In the provided test case, `test_first_odd`, the function is called with the list `[1,3,5]` and it is expected that the function will return `1`. After the function call, the message `"All tests passed"` is printed to the console.

You can run this code in a Python environment to test the function and ensure that it correctly identifies and returns the first odd number in a given list of numbers.
```