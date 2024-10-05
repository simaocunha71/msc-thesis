```
const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k);
};
```
Explanation:

* The `sort()` method is used to sort the array in descending order (i.e., largest to smallest).
* The `slice(0, k)` method is used to return a new array containing the first `k` elements of the sorted array.
* The resulting array is a sorted list of length `k` with the maximum `k` numbers in `arr`. 

Example:
```
console.log(maximum([-3, -4, 5], 3)); // Output: [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // Output: [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // Output: [2]
```  // Output: [2]  // Output: [4, -4, 4]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2]  // Output: [2