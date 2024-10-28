```
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
```


This function uses list comprehension to create a new list that includes only the elements from the original list that are even (i.e., where `i % 2 == 0`). The original list is left unchanged. 

The unit test `assert remove_odd([1,2,3]) == [2]` ensures that the function correctly identifies the even number in the list and removes the odd numbers. 

For example, if you call `remove_odd([1,2,3])`, the function will return `[2]`, which is the even number in the original list.  If you call `remove_odd([4,5,6])`, the function will return `[4,6]`, which are the even numbers in the original list.  If you call `remove_odd([7,8,9])`, the function will return `[8]`, which is the even number in the original list.  And so on.  In general, the function will return a list of all the even numbers from the original list, and will not include any odd numbers.  This is in accordance with the unit test, which checks that the function returns the correct result for the given input.  The unit test is `assert remove_odd([1,2,3]) == [2]`, which checks that the function returns `[2]` when given the input `[1,2,3]`.  This is the expected result, because `[2]` is the only even number in the original list.  The function passes this test, because it correctly identifies the even number in the list and removes the odd numbers.  Therefore, the function is correct and can be used to remove odd numbers from a given list. 