```
def two_unique_nums(lst):
    unique_nums = set(lst)
    return [num for num in unique_nums if lst.count(num) == 1]
```
This function works by first converting the list to a set, which automatically removes any duplicate numbers. Then it uses a list comprehension to iterate over the set and include only the numbers that appear only once in the original list. The count method is used to check if a number appears only once in the list. 

For example, if you call `two_unique_nums([1,2,3,2,3,4,5])`, the function will return `[1, 4, 5]`, which are the numbers that appear only once in the original list. 

The unit test `assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]` ensures that this function works correctly. 

Note: This function assumes that the input list contains only integers. If the list can contain other types of numbers (e.g. floats), you may need to modify the function accordingly. 

Also, this function has a time complexity of O(n^2) because it uses the count method, which has to iterate over the entire list for each number. If you need a more efficient solution, you can use a dictionary to count the occurrences of each number, which would reduce the time complexity to O(n). 

Here is the modified function:
```
def two_unique_nums(lst):
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    return [num for num, count in num_count.items() if count == 1]
```
This function uses a dictionary to count the occurrences of each number, and then uses a list comprehension to return the numbers that appear only once. This function has a time complexity of O(n), which is more efficient than the previous function. 