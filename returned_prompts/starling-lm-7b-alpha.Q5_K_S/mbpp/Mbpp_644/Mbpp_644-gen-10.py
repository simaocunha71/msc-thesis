Here is one way to do it:

```python
def reverse_Array_Upto_K(arr, k):
    for i in range(k+1):
        arr[i], arr[k-i] = arr[k-i], arr[i]
    return arr
```

And here's a more pythonic version using list slicing:

```python
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```

Both of these functions will reverse the array up to the kth position and return the result.

```python
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
```

To use the function, simply call it with the array and the desired position as arguments. The function will return the reversed array.

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))  # prints [4, 3, 2, 1, 5, 6]
```

This will print the result of the function call, which is [4, 3, 2, 1, 5, 6].

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],6))  # prints [6, 5, 4, 3, 2, 1]
```

This will print the result of the function call, which is [6, 5, 4, 3, 2, 1].

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],7))  # prints [6, 5, 4, 3, 2, 1]
```

This will print the result of the function call, which is [6, 5, 4, 3, 2, 1].

``