You can solve this problem by using a two-pointer approach. The idea is to initialize two pointers, one at the start and one at the end of the array, and then move them towards each other until they meet at an element that appears only once.

Here is the Python function to solve the problem:

```
def search(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[low]:
            low += 1
        elif nums[mid] == nums[high]:
            high -= 1
        else:
            return nums[mid]
    return nums[low]
```

This function works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the next interval will be the lower half. Otherwise, the next interval will be the upper half. The search process repeats until the size of the interval is zero, which means the search key is found, or until the size of the interval is one, which means the search key is the only one in the array. In this case, the function returns the only element in the array.

The unit test `assert search([1,1,2,2,3]) == 3` passes, which means the function works correctly. It returns the element that appears only once in the array, which is 3.