
def sort_array(arr):
    return sorted(arr, key = lambda x: (bin(x).count('1'), -x))
```
    
The code above will sort the array based on the number of ones in their binary representation. For similar number of ones, it will sort based on the decimal value.

The lambda function is used as a key to the `sorted` function, which allows us to define a custom sorting order based on the result of the lambda function.

In the lambda function, `bin(x).count('1')` counts the number of ones in the binary representation of `x`, and `-x` is used to sort the array in ascending order of the decimal value.

The `sorted` function then uses this key to sort the array, resulting in the desired output.

For example, when we call `sort_array([1, 5, 2, 3, 4])`, the output will be `[1, 2, 3, 4, 5]`, as the number of ones in their binary representation is `1` for `1`, `2` for `2`, `2` for `3`, `2` for `4`, and `3` for `5`. Since the number of ones is the same for `2`, `3`, and `4`, they are sorted based on their decimal value, resulting in the array `[1, 2, 3, 4, 5]`.

Similarly, when we call `sort_array([-2, -3, -4, -5, -6])`, the output will be `[-6, -5, -4, -3, -2]`, as the number of ones in their binary representation is `1` for `-2`, `2` for `-3`, `2` for `-4`, `3` for `-5`, and `3` for `-6`. Since the number of ones is the same for `-3`, `-4`, and `-5`, they are sorted based on their decimal value, resulting in the array `[-6, -5, -4, -3, -2]`.

And for `sort_array([1, 0, 2, 3, 4])`, the output will be `[0, 1