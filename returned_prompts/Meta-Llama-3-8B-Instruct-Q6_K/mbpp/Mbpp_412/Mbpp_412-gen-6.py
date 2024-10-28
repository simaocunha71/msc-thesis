```
def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]
``` 
Explanation:
The function `remove_odd` takes a list of numbers as input. It uses a list comprehension to create a new list that includes only the numbers that are divisible by 2 (i.e., even numbers). The `if` condition `num % 2 == 0` filters the numbers to include only the even ones. The function then returns this new list. 

The unit test `assert remove_odd([1,2,3]) == [2]` ensures that the function works correctly by checking that the output `[2]` matches the expected result. 
This function is case-insensitive and can handle lists of integers, floats, or mixed types. However, it assumes that the input list contains only numbers. If the list contains non-numeric values, the function will raise an error. 

The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate over the entire list once to create the output list. The space complexity is also O(n) because it needs to store the output list. 
```python
assert remove_odd([1,2,3]) == [2]
``` 
This unit test checks that the function correctly removes odd numbers from the input list. The expected output is `[2]`, which is the only even number in the input list. The actual output should match this expected output for the function to be considered correct. 