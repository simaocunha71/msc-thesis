Here is the solution using JavaScript:
```
const pluck = (arr) => {
  if (arr.length === 0) return [];
  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) return [];
  const smallestEvenValue = Math.min(...evenNodes);
  return [smallestEvenValue, arr.indexOf(smallestEvenValue)];
};
```
Here's an explanation of the solution:

1. First, we check if the input array is empty. If it is, we return an empty array.
2. We use the `filter()` method to create a new array `evenNodes` that contains only the even nodes from the original array.
3. If `evenNodes` is empty, it means there are no even values in the original array, so we return an empty array.
4. We use the `Math.min()` function to find the smallest even value in `evenNodes`.
5. Finally, we return an array containing the smallest even value and its index in the original array using the `indexOf()` method.

You can test the function with the examples provided in the problem statement to see that it works as expected. For example:
```
console.log(pluck([4, 2, 3])); // Output: [2, 1]
console.log(pluck([1, 2, 3])); // Output: [2, 1]
console.log(pluck([])); // Output: []
console.log(pluck([5, 0, 3, 0, 4, 2])); // Output: [0, 1]
```