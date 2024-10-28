
def sort_array(arr):
    def binary_ones(num):
        cnt = 0
        while num:
            cnt += 1
            num &= num - 1
        return cnt
    return sorted(arr, key=lambda x: (binary_ones(x), x))








```
```

```

```

```

```

```

```

```

```

```

```

```

```

```
```

```python
def sort_array(arr):
    def binary_ones(num):
        cnt = 0
        while num:
            cnt += 1
            num &= num - 1
        return cnt
    return sorted(arr, key=lambda x: (binary_ones(x), x))
```

In this Kata, you have to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. For similar number of ones, sort based on decimal value. It must be implemented like this:

```python
>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
True
>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
True
>>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
True
```

Here are some tips to get you started:

- The `sorted()` function takes an iterable and a `key` parameter. The `key` parameter is a function that takes one argument and returns a value that will be used for sorting.

- You can use a lambda function to return the number of ones in the binary representation of a number, and then sort the array based on the result.

- The `sorted()` function will sort the array in ascending order of the key values, and if two values have the same key, it will sort them