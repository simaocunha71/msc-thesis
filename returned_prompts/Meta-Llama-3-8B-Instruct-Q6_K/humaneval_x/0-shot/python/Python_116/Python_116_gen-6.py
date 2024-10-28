The function sort_array(arr) will take an array of non-negative integers as input and return a sorted array based on the number of ones in their binary representation in ascending order. For similar number of ones, the array will be sorted based on decimal value.

Here is a Python solution for the problem:

```
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```

This solution uses the built-in sorted function in Python, which sorts the input array based on the key function. The key function here is a lambda function that takes an element from the array and returns a tuple. The first element of the tuple is the count of ones in the binary representation of the number, and the second element is the number itself. The sorted function sorts the array based on these tuples, first by the count of ones and then by the number itself. This ensures that the array is sorted based on the number of ones in their binary representation in ascending order, and for similar number of ones, the array is sorted based on decimal value. 