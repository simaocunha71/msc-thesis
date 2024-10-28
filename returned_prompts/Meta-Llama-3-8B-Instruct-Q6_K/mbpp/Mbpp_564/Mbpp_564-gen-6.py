The problem asks to create a function that takes a list of integers and counts the number of possible unordered pairs where both elements are unequal. 

However, the problem statement seems to be missing a crucial piece of information, which is the value to which each pair should sum up to. 

Luckily, the unit test `assert count_Pairs([1,2,1],3) == 2` provides this missing information. It seems that the function should count the number of unordered pairs where both elements are unequal and their sum is equal to the given number (in this case, 3). 

Here's a Python function that solves the problem:

```
def count_Pairs(lst, target):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] + lst[j] == target:
                count += 1
    return count
```

This function works by iterating over the list and checking every pair of elements. If the elements are unequal and their sum is equal to the target, it increments the count. Finally, it returns the count. 

This function should pass the given unit test. However, please note that this function has a time complexity of O(n^2) due to the nested loops, where n is the length of the input list. If the input list is large, this function may be slow. For a more efficient solution, you may need to use a different approach. 