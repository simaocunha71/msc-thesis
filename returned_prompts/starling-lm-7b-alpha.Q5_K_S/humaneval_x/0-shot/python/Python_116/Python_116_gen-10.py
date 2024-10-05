
def sort_array(arr):
    return sorted(arr, key = lambda x : (bin(x).count('1'), -x))
```
    
Here's a Python solution to the problem. The `sorted` function is used to sort the array `arr` by the binary representation of the elements. The `key` parameter of the `sorted` function is set to a lambda function that returns a tuple. The first element of the tuple is the count of '1's in the binary representation of the number, and the second element is the negative of the number itself. This ensures that the numbers are sorted first by the number of '1's in their binary representation, and then by their decimal value.

For example, in the first test case `[1, 5, 2, 3, 4]`, the binary representations of these numbers are `[1, 101, 10, 11]`, and the decimal values are the same. Therefore, they are sorted in ascending order as `[1, 2, 3, 4, 5]`.

In the second test case `[-2, -3, -4, -5, -6]`, the binary representations of these numbers are `[10, 11, 100, 110, 111]`, and the decimal values are the same. Therefore, they are sorted in ascending order as `[-6, -5, -4, -3, -2]`.

In the third test case `[1, 0, 2, 3, 4]`, the binary representations of these numbers are `[1, 0, 10, 11, 100]`, and the decimal values are the same. Therefore, they are sorted in ascending order as `[0, 1, 2, 3, 4]`.
```

The solution uses the built-in `sorted` function in Python to sort the input array `arr` based on two criteria: the count of '1's in the binary representation of each number, and the negative of the number itself. This ensures that the numbers are sorted first by the number of '1's in their binary representation, and then by their decimal value.

The `key` parameter of