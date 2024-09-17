```
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
```


Here, we are using list comprehension to filter out the odd numbers from the given list. The condition `i % 2 == 0` checks if a number is even, and if it is, it is included in the new list. The function returns this new list. 

This solution is in accordance with the unit test provided: `assert remove_odd([1,2,3]) == [2]`. The function should return a list that includes only the even number from the original list. 

For example, if the input list is `[1,2,3]`, the function will return `[2]`, which is the only even number in the list. If the input list is `[4,5,6]`, the function will return `[4,6]`, which are the even numbers in the list. 

This solution is efficient as it has a time complexity of O(n), where n is the number of elements in the list. This is because it needs to iterate over the list once to filter out the odd numbers. 

The space complexity is also O(n), as it needs to create a new list to store the even numbers. 

This solution is also easy to understand and maintain, as it is a simple and straightforward implementation of the required functionality. 