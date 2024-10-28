
Here is a Python solution to the Pluck problem:

```
def pluck(arr):
    if len(arr) == 0:
        return []
    smallest_value = min(i for i in arr if i % 2 == 0)
    smallest_index = arr.index(smallest_value)
    return [smallest_value, smallest_index]
```

Explanation:
- The `pluck` function takes an array of non-negative integers as input.
- It first checks if the array is empty and if so, it returns an empty list.
- Then, it uses a generator expression to find the smallest even value in the array.
- It uses the `min` function to find the minimum value from the generator expression.
- Next, it finds the index of the smallest even value in the array using the `index` method.
- Finally, it returns a list containing the smallest even value and its index.

This solution has a time complexity of O(n) because it needs to iterate through the array once to find the smallest even value and its index.

Here are some examples of how the `pluck` function can be used:

```python
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```

In the first example, the smallest even value is 2 and it has the smallest index of 1, so the output is [2, 1].
In the second example, the smallest even value is also 2 and it has the smallest index of 1, so the output is [2, 1].
In the third example, there are no even values or the array is empty, so the output is [].
In the fourth example, the smallest even value is 0 and it appears twice, but the first occurrence has the smallest index of 1, so the output is [0, 1].

Hope this helps!
```

``