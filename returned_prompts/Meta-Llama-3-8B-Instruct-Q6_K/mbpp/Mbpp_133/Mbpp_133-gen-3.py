```
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)
```


This function uses a generator expression to iterate over the list and sum up the numbers that are less than 0. The built-in `sum` function is used to calculate the sum. 

The unit test provided, `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32`, ensures that the function works correctly.  It checks that the sum of the negative numbers in the list is `-32`, which is the expected output. 

This function is more concise and efficient than a traditional loop, especially for large lists. It also clearly expresses the intention of the code, which is to sum up the negative numbers in the list.  The use of a generator expression makes it easy to read and understand. 

The function does not modify the original list, it only iterates over it and returns a new value. This makes it a pure function, which is a good practice in functional programming.  It also means that the function can be safely used in parallel or concurrently without worrying about unintended side effects.  The function is also easy to test, as it has a clear and well-defined output.  This makes it a good example of a well-designed and well-implemented function. 