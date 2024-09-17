```
def search(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]
```
The function iterates over the array, and whenever it finds a number that is different from the next one, it returns that number. If no such number is found, it returns the last number in the array, which is the one that appears only once. This solution assumes that the array is sorted and that all other numbers appear twice. It also assumes that the array is not empty. If these assumptions are not correct, the function may not work correctly. The unit test `assert search([1,1,2,2,3]) == 3` helps to clarify the expected behavior of the function. 

The time complexity of this function is O(n), where n is the number of elements in the array, because it needs to iterate over the entire array. The space complexity is O(1), because it only uses a constant amount of space. 