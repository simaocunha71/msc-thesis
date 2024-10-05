Here is the Python solution for the problem:

```python
def add_elements(arr, k):
    return sum([num for num in arr[:k] if len(str(abs(num))) <= 2])

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # Output: 24
```

Explanation:
The function `add_elements(arr, k)` takes two parameters: `arr`, which is the input array of integers, and `k`, which is the number of elements to consider from the beginning of the array.

The function uses a list comprehension to generate a list of numbers from the first `k` elements of `arr` that have at most two digits. It uses the `len(str(abs(num))) <= 2` condition to check if a number has at most two digits.

Finally, the function returns the sum of the generated list of numbers.

In the example given in the problem, the function will return the sum of the numbers 21 and 3, which is 24.