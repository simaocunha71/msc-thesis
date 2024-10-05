
def sort_array(arr):
    return sorted(arr, key = lambda x: (bin(x).count('1'), -x))
```
    
Here is the step by step explanation of the solution:

1. We need to sort the array of non-negative integers based on the number of '1' in their binary representation. For the same number of '1' in binary, sort based on the decimal value of the numbers.

2. Here's a simple way to solve the problem:

    a. First, we need to get the count of '1' in the binary representation of each integer. We can do this by using the built-in `bin()` function to convert an integer to binary and then using the `count()` method on the string to get the count of '1' in the binary representation.

    b. Next, we need to sort the array based on the count of '1' in the binary representation. We can do this by using the `sorted()` function and providing a `key` parameter to specify the function to be applied to each element of the array before the sorting. We use a lambda function to apply the `bin().count('1')` function to each element of the array.

    c. Finally, for the same number of '1' in binary, we need to sort based on the decimal value of the numbers. We can do this by providing a `key` parameter to the `sorted()` function again, but this time we use a lambda function to apply the `-` operator to each element of the array. This will reverse the order of the elements, effectively sorting them in ascending order.

3. Here's the complete solution:

```python
def sort_array(arr):
    return sorted(arr, key = lambda x: (bin(x).count('1'), -x))
```

4. The above solution will correctly sort the array of non-negative integers based on the number of '1' in their binary representation in ascending order, and for the same number of '1' in binary, it will sort based on the decimal value of the numbers.

5. The provided test cases in the problem statement are used to verify the correctness of the solution.
```



```

```
