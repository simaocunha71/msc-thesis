Here is a solution for the problem. It uses the built-in JavaScript methods `set` and `Array.from` to find the common elements and then sorts them.

```javascript
const common = (l1, l2) => {
  return Array.from(new Set([...l1, ...l2]).filter(x => l1.includes(x) && l2.includes(x))).sort((a, b) => a - b);
};

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])); // [1, 5, 653]
console.log(common([5, 3, 2, 8], [3, 2])); // [2, 3]
```

This solution works as follows:

- `Set([...l1, ...l2])` creates a set of all unique elements from both lists.
- `filter(x => l1.includes(x) && l2.includes(x))` filters the set to only include elements that are present in both lists.
- `Array.from` converts the filtered set back to an array.
- `sort((a, b) => a - b)` sorts the array in ascending order.
- The resulting array is then returned.

This solution has a time complexity of O(n log n) due to the sorting, where n is the total number of elements in both lists. The space complexity is O(n) as we need to store the set and the resulting array. 