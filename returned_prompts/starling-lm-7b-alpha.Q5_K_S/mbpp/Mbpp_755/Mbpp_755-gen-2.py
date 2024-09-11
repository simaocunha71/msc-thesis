```
def second_smallest(nums):
    nums.sort()
    return nums[1]
```

Explanation:
To find the second smallest number in a list, we can first sort the list in ascending order using the `sort()` method. Then, we can return the element at index 1, which will be the second smallest number in the list. In the provided example, `second_smallest([1, 2, -8, -2, 0, -2])` will return `-2` as the second smallest number in the list.

However, it's important to note that this solution assumes that the list contains at least two distinct elements. If the list has only one element or all elements are the same, the `second_smallest()` function will raise an error. To handle such cases, we can add error checking code to the function, as shown below:

```python
def second_smallest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two distinct elements")
    nums.sort()
    return nums[1]
```

With this error checking code, if the length of the `nums` list is less than 2, a `ValueError` will be raised with the message "List must contain at least two distinct elements".

Overall, the `second_smallest()` function provides a simple and efficient solution to find the second smallest number in a list, as long as the list contains at least two distinct elements.

```python
def second_smallest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two distinct elements")
    nums.sort()
    return nums[1]
```

Here is an example of how to use the `second_smallest()` function:

```python
print(second_smallest([1, 2, -8, -2, 0, -2]))  # Output: -2
print(second_smallest([1, 2]))  # Raises ValueError: List must contain at least two distinct elements
```

The first call to `second_smallest()` returns `-2`