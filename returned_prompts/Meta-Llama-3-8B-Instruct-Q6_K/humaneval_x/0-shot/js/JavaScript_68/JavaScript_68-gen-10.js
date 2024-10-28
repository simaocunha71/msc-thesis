Here is the solution to the problem:

```javascript
const pluck = (arr) => {
  let smallestValue = Infinity;
  let smallestIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallestValue) {
      smallestValue = arr[i];
      smallestIndex = i;
    }
  }
  return smallestValue === Infinity ? [] : [smallestValue, smallestIndex];
};
```

Explanation:

1. We initialize `smallestValue` to `Infinity` and `smallestIndex` to `-1`.
2. We iterate through the array using a `for` loop.
3. For each node, we check if it's even (`arr[i] % 2 === 0`) and if its value is smaller than the current `smallestValue`. If both conditions are true, we update `smallestValue` and `smallestIndex` with the current node's value and index, respectively.
4. After iterating through the entire array, we check if `smallestValue` is still `Infinity`. If it is, that means there were no even values in the array, so we return an empty array. Otherwise, we return an array containing the smallest even value and its index.

This solution has a time complexity of O(n), where n is the length of the input array, because we iterate through the array once. The space complexity is O(1), because we only use a constant amount of space to store the smallest value and index.