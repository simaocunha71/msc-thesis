To solve this problem, you can follow these steps:

1. Create an empty set `seen` to keep track of the elements that have been seen.
2. Create an empty array `res` to store the unique elements.
3. Iterate through the input list `l`. For each element `x`, perform the following steps:
   - Check if `x` is not in the `seen` set. If it is not in the set, then it has not been seen before. In this case, add `x` to the `res` array and update the `seen` set by adding `x`.
4. After iterating through all the elements in `l`, return the `res` array, which will contain all the unique elements in sorted order.

Here is the implementation of the solution in JavaScript:

```javascript
const unique = (l) => {
  const seen = new Set();
  const res = [];

  for (let x of l) {
    if (!seen.has(x)) {
      seen.add(x);
      res.push(x);
    }
  }

  return res.sort((a, b) => a - b);
};
```

This implementation uses a set `seen` to efficiently check if an element has been seen before. The `seen` set only allows unique values, so checking if an element is in the set is a fast operation. The `res` array is used to store the unique elements in the order they appear in the input list. Finally, the `res` array is sorted using the `sort` method with a compare function to ensure the elements are sorted in ascending order.

The time complexity of this solution is O(n), where n is the length of the input list. This is because each element in the list is processed exactly once. The space complexity is also O(n), as we need to store all the unique elements in the `res` array and the `seen` set.

You can use this `unique` function to get the sorted unique elements from a list. For example, if you call `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])`, it will return `[0, 2, 3, 5, 9, 1