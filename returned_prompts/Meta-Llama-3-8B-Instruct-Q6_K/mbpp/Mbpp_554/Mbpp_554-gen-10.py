```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```
The function `Split` takes a list of integers as input and returns a new list containing only the odd numbers from the input list. The list comprehension `[i for i in lst if i % 2 != 0]` iterates over the input list and includes only the elements for which the remainder when divided by 2 is not 0, which means only the odd numbers.  The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` ensures that the function works correctly. 

This function uses list comprehension which is a shorthand way of creating lists in Python. It consists of brackets containing an expression followed by a for clause. The list comprehension will iterate over the items in the list and include them in the new list if the condition specified in the if clause is met. 

The `i % 2 != 0` condition is used to check if the number is odd. In Python, the modulus operator `%` returns the remainder of the division of the number before it by the number after it. If the remainder is not 0, then the number is odd. If the remainder is 0, then the number is even. Therefore, the list comprehension will include only the numbers for which the remainder when divided by 2 is not 0, which means only the odd numbers. 