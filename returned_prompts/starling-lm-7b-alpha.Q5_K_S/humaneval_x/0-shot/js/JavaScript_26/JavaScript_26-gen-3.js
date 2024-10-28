To solve this problem, you can use a Set. A Set is a collection of unique values. Here's how you can use it to solve this problem:

1. Initialize an empty Set called `seen` to keep track of the unique values you've already seen.
2. Iterate over the `numbers` array using the `forEach` method. For each number `n` in the array:
    - If `n` is not in the `seen` Set, add it to the Set and the `result` array.
3. Return the `result` array.

Here's the code that implements this solution:

```javascript
const removeDuplicates = (numbers) => {
  const seen = new Set();
  const result = [];

  numbers.forEach((n) => {
    if (!seen.has(n)) {
      seen.add(n);
      result.push(n);
    }
  });

  return result;
};
```

The time complexity of this solution is O(n), where n is the length of the `numbers` array. This is because we need to iterate over the array once to check each number. The space complexity is also O(n), as we need to store each unique number in the `seen` Set and the `result` array.

To test the solution, you can use the following code:

```python
print(removeDuplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This will print the result of calling the `removeDuplicates` function with the input `[1, 2, 3, 2, 4]`. The output will be `[1, 3, 4]`, which are the unique elements from the input array in the same order.

Here is the Python code for the solution:

```python
def removeDuplicates(numbers):
    seen = set()
    result = []

    for n in numbers:
        if n not in seen:
            seen.add(n)
            result.append(n)

    return result
```

And here is how you can test the solution:

``