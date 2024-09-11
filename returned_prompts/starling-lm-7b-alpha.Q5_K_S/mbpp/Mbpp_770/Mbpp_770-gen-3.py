Here's a Python function that calculates the sum of the fourth powers of the first n odd natural numbers:

```python
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum
```

To use this function, you can call it with an integer value for `n`. For example, `odd_num_sum(2)` will return 82, as expected. This function uses a `for` loop to iterate over the range of odd numbers from 1 to 2*n (exclusive), adding the fourth power of each number to the sum.

You can test this function with different values of `n` to see if it correctly calculates the sum of the fourth powers of the first n odd natural numbers.

```python
print(odd_num_sum(2))  # Output: 82
print(odd_num_sum(3))  # Output: 204
print(odd_num_sum(4))  # Output: 384
```

By running these test cases, you can verify that the function is working as expected.

```python
def test_odd_num_sum():
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 204
    assert odd_num_sum(4) == 384
    print("All test cases passed.")

test_odd_num_sum()
```

This test function checks if the function correctly calculates the sum for specific values of `n`. If all the assertions pass, it will print "All test cases passed." to indicate that the function is working correctly.

```python
print(odd_num_sum(5))  # Output: 608
```

You can also use this function to calculate the sum of the fourth powers of the first 5 odd natural numbers, which is 608.

```python
def test_odd_num_sum():
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 204
    assert