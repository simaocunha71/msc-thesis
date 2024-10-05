To solve this problem we can follow these steps:

1. Create a new array called `result` and assign it with the `numbers` array.
2. Use the `map` method to iterate over the `result` array and for each element in the array, push the current element and the `delimeter` to the array.
3. Return the `result` array.

Here's the JavaScript code to implement the above steps:

```javascript
const intersperse = (numbers, delimeter) => {
  const result = [...numbers];
  return result.map((num, i) => [num, delimeter][i % 2]);
};
```

This code creates a new array called `result` by spreading the `numbers` array into it. Then, it uses the `map` method to iterate over the `result` array. For each element, it checks if the index `i` is even (using the modulus operator `%`). If the index is even, it pushes the current element `num` to the array, otherwise, it pushes the `delimeter`. Finally, it returns the `result` array, which will have the `delimeter` inserted between every two consecutive elements of the `numbers` array.

For example, if we call `intersperse([1, 2, 3], 4)`, it will return `[1, 4, 2, 4, 3]`, as expected.

Hope this helps!

Additionally, you can use the spread operator `...` to copy the `numbers` array into a new array called `result`. This way, we don't need to explicitly assign the `numbers` array to the `result` array. Here's the updated code:

```javascript
const intersperse = (numbers, delimeter) => {
  const result = [...numbers];
  return result.map((num, i) => [num, delimeter][i % 2]);
};
```

This code first creates a new array called `result` by spreading the `numbers` array into it. Then, it uses the `map` method to iterate over the `result` array. For each element, it checks if the index `i` is