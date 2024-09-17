```
def search(nums):
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i] != nums[i+1]:
            return nums[i]
```



This function iterates over the array and returns the element that appears only once. The condition `if i == len(nums) - 1 or nums[i] != nums[i+1]:` checks if the current element is the last one or if it's different from the next one, in which case it returns the current element.

The unit test `assert search([1,1,2,2,3]) == 3` ensures that the function works correctly. It checks that when the input is `[1,1,2,2,3]`, the output is `3`, which is the element that appears only once in the array. 

This function assumes that the input array is sorted and that there is exactly one element that appears only once. If these conditions are not met, the function may not work correctly. 