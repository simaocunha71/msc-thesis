def swap_List(nums):
    tmp = nums[0]
    nums[0] = nums[-1]
    nums[-1] = tmp
    return nums


def test_swap_List():
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]

test_swap_List()












































```
```

```

```

```
```
```

```python
def swap_List(nums):
    tmp = nums[0]
    nums[0] = nums[-1]
    nums[-1] = tmp
    return nums
```

In this function, we define a function called `swap_List` that takes a list of numbers as an argument. The function first stores the value of the first element in a temporary variable called `tmp`. Then, it assigns the value of the last element to the first element and assigns the value of `tmp` to the last element. Finally, it returns the modified list.

To test the function, we define a function called `test_swap_List` that asserts that the function `swap_List` returns the expected result when given the input `[12, 35, 9, 56, 24]`. 

When we run the test, it will compare the result of `swap_List([12, 35, 9, 56, 24])` with the expected result `[24, 35, 9, 56, 12]`. If the results are the same, the test will pass; otherwise, it will fail.

This code ensures that the function `swap_List` correctly interchanges the first and last elements in a list.

```python
```
```

```python
```
```

```python
```
```
```
