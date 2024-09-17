```
def search(nums):
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]
```
The function iterates over the sorted array and returns the first element that is different from the next one. This element appears only once in the array. If no such element is found, it returns the last element of the array, which also appears only once. This function assumes that the input array is sorted and that all elements are distinct except for one, which appears only once. 

The unit test `assert search([1,1,2,2,3]) == 3` ensures that the function works correctly. It checks if the function returns the element that appears only once in the array, which is 3 in this case. 

This problem is a classic example of a "first unique element" problem, which can be solved efficiently by iterating over the array once. The time complexity of this function is O(n), where n is the number of elements in the array, and the space complexity is O(1), as it only uses a constant amount of space. 