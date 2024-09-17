```
def _sum(array):
    return sum(array)
```
This function uses the built-in `sum` function in Python to find the sum of the elements in the given array. The unit test `assert _sum([1, 2, 3]) == 6` ensures that the function works correctly for a simple example. 

However, the problem statement seems to be asking for a function that takes an array as input and returns its sum. The `sum` function in Python already does this, so we can simply use it directly without writing our own implementation. 

If we were to write our own implementation, it would look something like this:
```
def _sum(array):
    total = 0
    for num in array:
        total += num
    return total
``` 
This function initializes a variable `total` to 0, then iterates over each number in the array, adding it to `total`. Finally, it returns the total sum.  However, using the built-in `sum` function is generally more efficient and easier to read. 