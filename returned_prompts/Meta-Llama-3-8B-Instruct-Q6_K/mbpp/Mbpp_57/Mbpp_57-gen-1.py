The problem is asking to find the largest number that can be formed using the given list of digits. 

We can solve this problem by first sorting the list of digits in descending order and then joining them together to form the largest number.

Here is the python function that does this:

```
def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True))))
```

This function works by first converting each digit to a string using the `map` function, then sorting the list of strings in descending order using the `sorted` function with the `reverse=True` argument, and finally joining the sorted strings together into a single string using the `join` function. The `int` function is used to convert the resulting string back to an integer.

For example, if we call `find_Max_Num([1,2,3])`, it will return `321`, which is the largest number that can be formed using the digits 1, 2, and 3. 

The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function is working correctly.  If the function is not working correctly, the test will fail and we will know that there is a bug in the function.  This can help us to debug the function and make sure it is working correctly. 