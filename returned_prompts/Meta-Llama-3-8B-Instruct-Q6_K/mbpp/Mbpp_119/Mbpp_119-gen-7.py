```
def search(nums):
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            return nums[i]
```


Explanation:
This problem is asking to find the element that appears only once in a sorted array. The function should iterate over the array and return the first element that is different from the previous one.

In the given unit test, `search([1,1,2,2,3])` should return `3` because `3` is the only element that appears only once in the array.

The solution uses a simple iteration over the array. It checks if the current element is different from the previous one. If it is, it returns the current element. If it's not, it continues to the next iteration. This way, it finds the first element that appears only once in the array. The time complexity of this solution is O(n), where n is the length of the array. The space complexity is O(1), as it only uses a constant amount of space.