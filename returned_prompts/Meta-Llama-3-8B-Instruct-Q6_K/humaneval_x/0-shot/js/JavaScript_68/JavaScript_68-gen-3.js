Here is the solution in JavaScript:
```javascript
const pluck = (arr) => {
  const evenNodes = arr.filter((node) => node % 2 === 0);
  if (evenNodes.length === 0) return [];
  const smallestEvenValue = Math.min(...evenNodes);
  const smallestEvenIndex = arr.findIndex((node) => node === smallestEvenValue);
  return [smallestEvenValue, smallestEvenIndex];
};
```
Here's an explanation of the code:

1. `arr.filter((node) => node % 2 === 0)` filters the array to get only the nodes with even values.
2. If the filtered array is empty, it means there are no even values, so we return an empty array `[]`.
3. `Math.min(...evenNodes)` finds the smallest even value.
4. `arr.findIndex((node) => node === smallestEvenValue)` finds the index of the smallest even value in the original array.
5. We return a list containing the smallest even value and its index.

You can test the function with the examples provided:
```javascript
console.log(pluck([4, 2, 3])); // Output: [2, 1]
console.log(pluck([1, 2, 3])); // Output: [2, 1]
console.log(pluck([])); // Output: []
console.log(pluck([5, 0, 3, 0, 4, 2])); // Output: [0, 1]
```  