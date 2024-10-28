```
def search(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]
```



The given problem is to find the element that appears only once in a sorted array. 

The unit test `assert search([1,1,2,2,3]) == 3` suggests that the function should return the first element that appears only once in the array. 

Here is a python function that solves this problem:

```
def search(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]
```

This function iterates over the array and returns the first element that is different from the next element. If no such element is found, it returns the last element, which is the only element that can appear only once in a sorted array. 

The time complexity of this function is O(n), where n is the number of elements in the array. The space complexity is O(1), as it only uses a constant amount of space. 