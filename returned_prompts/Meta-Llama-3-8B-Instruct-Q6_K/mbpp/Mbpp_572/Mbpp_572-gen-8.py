```
def two_unique_nums(nums):
    return list(set(nums))
```


In this function, we are using the set data structure to remove the duplicate numbers from the given list. The set data structure in Python is an unordered collection of unique elements. When you convert a list to a set, it automatically removes any duplicate values. We then convert the set back to a list and return it. Note that this function does not preserve the original order of the numbers, and it does not work correctly if the input list contains more than two unique numbers. 

If you need to preserve the original order and remove more than two unique numbers, you can use a different approach. For example, you can use a dictionary to keep track of the numbers you have seen so far, and then iterate over the list again to build the result. Here is an example of how you can do this:
```
def two_unique_nums(nums):
    seen = {}
    result = []
    for num in nums:
        if num not in seen:
            result.append(num)
            seen[num] = True
    return result
```
This function iterates over the input list, and for each number, it checks if the number has been seen before. If not, it adds the number to the result list and marks it as seen. This way, it preserves the original order of the numbers and removes all duplicate numbers. 

Note that this function has a time complexity of O(n), where n is the length of the input list, because it needs to iterate over the list twice (once to build the set and once to build the result). The space complexity is also O(n), because it needs to store all the unique numbers in the result list. 

If you need to remove duplicate numbers from multiple lists, you can use a similar approach. Here is an example of how you can do this:
```
def remove_duplicates(*lists):
    seen = {}
    result = []
    for nums in lists:
        for num in nums:
            if num not in seen:
                result.append(num)
                seen[num] = True
    return result
```
This function takes a variable number of lists as input, and it returns a new list that contains all the unique numbers from the input lists. It uses a dictionary to keep track of the numbers it has seen so far, and it iterates over each input list to build the result. This way, it preserves the original order of the numbers and removes all duplicate numbers. 

Note that this function