def move_zero(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[i+zero_count] = nums[i+zero_count], nums[i]
    return nums

# assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]









# Explanation:
# First, we count the number of zeroes in the given list and store them in the zero_count variable.
# Then, we iterate through the list and if the current number is not zero, we swap it with the number at the position zero_count from the end of the list. This moves the non-zero number to the correct position at the beginning of the list.
# After the iteration, all the non-zero numbers will be at the beginning of the list and the zeroes will be at the end.
# Finally, we return the modified list.

```python
def move_zero(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[i+zero_count] = nums[i+zero_count], nums[i]
    return nums
```
The above code defines a function called `move_zero` which takes a list of numbers as input. It first counts the number of zeroes in the list and stores it in the `zero_count` variable. Then, it iterates through the list and for each non-zero number, it swaps it with the number at the position `zero_count` from the end of the list. After the iteration, all the non-zero numbers will be at the beginning of the list and the zeroes will be at the end. Finally, it returns the modified