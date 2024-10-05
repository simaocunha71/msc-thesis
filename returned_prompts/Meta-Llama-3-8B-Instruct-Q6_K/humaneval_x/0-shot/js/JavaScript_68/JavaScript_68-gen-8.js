Here is a possible solution in JavaScript:
```
const pluck = (arr) => {
  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) return [];
  const smallestEvenValue = Math.min(...evenNodes);
  return [smallestEvenValue, arr.indexOf(smallestEvenValue)];
};
```
Here's an explanation of the solution:

1. First, we filter the array to get an array of only the even nodes using the `filter()` method.
2. If the resulting array is empty, we return an empty array `[]`.
3. We find the smallest even value using the `Math.min()` function with the spread operator `...`.
4. We then return an array containing the smallest even value and its index in the original array using the `indexOf()` method.

You can test the function with the examples provided:
```
console.log(pluck([4, 2, 3])); // Output: [2, 1]
console.log(pluck([1, 2, 3])); // Output: [2, 1]
console.log(pluck([])); // Output: []
console.log(pluck([5, 0, 3, 0, 4, 2])); // Output: [0, 1]
```
Note that this solution has a time complexity of O(n), where n is the length of the input array, since we are using the `filter()` and `indexOf()` methods, which have a linear time complexity. The space complexity is O(n) as well, since we are storing the filtered array in memory. However, this solution is simple and easy to understand, and it should be efficient enough for small to medium-sized input arrays. If you need a more efficient solution for very large input arrays, you may want to consider using a more advanced data structure or algorithm.