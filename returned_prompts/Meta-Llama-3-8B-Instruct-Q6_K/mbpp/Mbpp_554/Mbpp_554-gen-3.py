```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```


Explanation:
This function uses list comprehension to create a new list that includes only the elements from the input list that are odd. The condition `i % 2 != 0` checks if a number is odd, because odd numbers leave a remainder when divided by 2. If the number is odd, it is included in the new list. 

The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` ensures that the function is working correctly. It checks that the output of the function is `[1,3,5]` when the input is `[1,2,3,4,5,6]`. This confirms that the function is correctly identifying and returning the odd numbers. 





