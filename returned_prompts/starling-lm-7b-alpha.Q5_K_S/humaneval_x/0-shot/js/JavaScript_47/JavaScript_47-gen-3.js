To solve this problem, we can follow these steps:

1. Sort the list in ascending order.
2. Find the middle element(s) of the sorted list. If the length of the list is even, take the average of the two middle elements.
3. Return the median value(s).

Here's the step-by-step solution:

1. Sort the list in ascending order: `l.sort((a, b) => a - b)`.
2. Find the middle element(s) of the sorted list: `let median`.
   - If the length of the list is odd, assign `l[Math.floor(l.length / 2)]` to `median`.
   - If the length of the list is even, assign `(l[l.length / 2 - 1] + l[l.length / 2]) / 2` to `median`.
3. Return the median value(s): `return median`.

Here's the code for the solution:

```javascript
const median = (l) => {
  l.sort((a, b) => a - b);
  let median;
  if (l.length % 2 === 0) {
    median = (l[l.length / 2 - 1] + l[l.length / 2]) / 2;
  } else {
    median = l[Math.floor(l.length / 2)];
  }
  return median;
};
```

This implementation will correctly calculate the median for any given list.

To test the function, you can use the provided test cases:

```javascript
console.log(median([3, 1, 2, 4, 5]));  // Output: 3
console.log(median([-10, 4, 6, 1000, 10, 20]));  // Output: 8.0
```

These test cases will pass with the provided solution.

Additionally, if you want to support decimal numbers in the list, you can modify the `median` function as follows:

```javascript
const median = (l) => {
  l.sort((a,