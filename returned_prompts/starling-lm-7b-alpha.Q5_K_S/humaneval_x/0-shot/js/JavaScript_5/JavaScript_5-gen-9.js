Here's a possible solution to this problem:

```javascript
const intersperse = (numbers, delimeter) => {
  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i < numbers.length - 1) {
      result.push(delimeter);
    }
  }
  return result;
};
```

This function uses a `for` loop to iterate through the `numbers` array. For each element, it adds the element to a `result` array, and if the current index is not the last index, it also adds a `delimeter` to the `result` array. After iterating through all the elements, it returns the `result` array.

For example, if you call `intersperse([1, 2, 3], 4)`, it will return `[1, 4, 2, 4, 3]`.

Note that this solution assumes that the `numbers` array is not empty. If it's possible that `numbers` can be empty, you may want to add a check at the beginning of the function to handle this case.

Here's an updated version of the function that includes this check:

```javascript
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) {
    return [];
  }

  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i < numbers.length - 1) {
      result.push(delimeter);
    }
  }
  return result;
};
```

This version of the function first checks if `numbers` is empty, and if so, it returns an empty array. Otherwise, it proceeds with the original logic of adding each number to the `result` array, with a `delimeter` in between if necessary.

With this update, if you call `intersperse([], 4)`, it will return `[]`, as expected.

Overall, this function provides a straightforward and efficient way to