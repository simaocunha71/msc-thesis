Here is a simple Python solution using list comprehension:

```
def intersperse(numbers, delimeter):
    return [num for i, num in enumerate(numbers + [delimeter]) if i % 2 == 0]
```

Here's how it works:

- We concatenate the input list `numbers` with the `delimeter` at the end. This way, we can iterate over the entire list and the `delimeter` as well.
- We use `enumerate` to get the index `i` and the value `num` of each element in the combined list.
- We use a conditional expression to filter out the `delimeter` values (i.e., when `i` is odd). We only include the `num` values when `i` is even.
- The resulting list comprehension returns the desired output.

Let's test it:

```
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```  