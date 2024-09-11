Here is a Python function that takes an array and a position and returns the reversed array upto the given position:

```python
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```

To use this function, you can call it with the array and the position as arguments and check if the result is correct using the `assert` keyword.

For example:

```python
def test_reverse_Array_Upto_K():
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
    print("All tests passed!")

test_reverse_Array_Upto_K()
```

In this test case, the function `reverse_Array_Upto_K` is called with the array `[1, 2, 3, 4, 5, 6]` and the position `4`. The expected result is `[4, 3, 2, 1, 5, 6]`. The `assert` statement checks if the result of the function call is equal to the expected result. If the condition is true, the message `"All tests passed!"` is printed. Otherwise, an error is raised.

This test case verifies that the function `reverse_Array_Upto_K` correctly reverses the array upto the given position.

```python
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```

This function takes two arguments: `arr`, the array to be reversed, and `k`, the position upto which the array should be reversed. The function uses Python's slicing feature to reverse the array upto the given position. The slice `arr[:k]` selects all elements from the beginning of the array up to the position `k`, and the `[::-1]` part reverses the selected elements. The slice `arr[k:]` selects all elements from the position `k` to the end of the array. The `+` operator conc