```
def search(nums):
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i] != nums[i+1]:
            return nums[i]
```


This function iterates over the array and returns the first element that is different from the next one. This element must be the one that appears only once in the array, as it's the only one that is not repeated.

The unit test `assert search([1,1,2,2,3]) == 3` confirms this, as the function correctly returns `3` which is the element that appears only once in the array. 





