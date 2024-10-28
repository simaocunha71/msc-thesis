Here is the solution:

```javascript
const removeDuplicates = (numbers) => {
  let seen = {};
  let result = [];
  for (let num of numbers) {
    if (!seen[num]) {
      seen[num] = true;
      result.push(num);
    }
  }
  return result;
};
```

Explanation:

*   We create an object `seen` to keep track of the numbers we have seen so far.
*   We create an empty array `result` to store the unique numbers.
*   We iterate over the input array `numbers`.
*   For each number, we check if it is already in the `seen` object. If it is not, we add it to the `seen` object and the `result` array.
*   Finally, we return the `result` array.

This solution has a time complexity of O(n), where n is the length of the input array, because we make a single pass over the array. The space complexity is also O(n), because in the worst case, we might need to store all numbers in the `seen` object and the `result` array.