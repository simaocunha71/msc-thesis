Here is the solution to the problem:

```javascript
const pluck = (arr) => {
  if (!arr.length) return [];

  const evenNodes = arr.filter((node) => node % 2 === 0);
  if (!evenNodes.length) return [];

  const smallestEvenValue = Math.min(...evenNodes);
  const smallestEvenNodeIndex = arr.findIndex((node) => node === smallestEvenValue);

  return [smallestEvenValue, smallestEvenNodeIndex];
};
```

This function first checks if the array is empty. If it is, it returns an empty array.

Then, it filters the array to get only the even nodes. If there are no even nodes, it returns an empty array.

Next, it finds the smallest even value and its index in the original array.

Finally, it returns a list containing the smallest even value and its index. If there are multiple nodes with the same smallest even value, it returns the one with the smallest index. If there are no even values, it returns an empty array.