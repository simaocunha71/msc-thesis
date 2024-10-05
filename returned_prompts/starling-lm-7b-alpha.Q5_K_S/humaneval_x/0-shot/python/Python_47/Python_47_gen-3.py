
Here are some tips to solve this problem:

1. Sort the list in ascending order. You can use the `sort()` method to sort the list in place. After sorting, the median is just the middle element.
2. If the list has an even number of elements, the median is the average of the two middle elements. You can find the average by adding the two middle elements and dividing the result by 2.
3. To find the middle element(s), you can use integer division (`//`) to get the index of the middle element(s) and access the element(s) using that index.

Here's a step-by-step solution:

1. Sort the list using the `sort()` method: `l.sort()`.
2. Determine the length of the list, `n`, using the `len()` function: `n = len(l)`.
3. Check if the length of the list is odd or even using the modulo operator (`%`):
   - If `n % 2 == 0`, the length is even, and the median is the average of the two middle elements.
   - If `n % 2 == 1`, the length is odd, and the median is the middle element.
4. Calculate the index of the middle element(s) using integer division (`//`): `middle_index = n // 2`.
5. If the length is even, return the average of the two middle elements: `(l[middle_index - 1] + l[middle_index]) / 2`.
6. If the length is odd, return the middle element: `l[middle_index]`.

Here's the complete solution:

```python
def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 0:
        middle_index = n // 2
        return (l[middle_index - 1] + l[middle_index]) / 2
    else:
        middle_index = n // 2
        return l[middle_index]
```

You can now use the `median()` function to find the median of a list of elements:

```python
print(med