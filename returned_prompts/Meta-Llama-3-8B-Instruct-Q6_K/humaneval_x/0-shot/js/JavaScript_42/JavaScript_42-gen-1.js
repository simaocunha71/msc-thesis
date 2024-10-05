Here is a simple solution using a map function in JavaScript:
```
const incrList = (l) => l.map(x => x + 1);
```
Explanation:

*   The `map` function is used to create a new array by applying a transformation to each element of the original array `l`.
*   The transformation is a function that takes an element `x` and returns its value incremented by 1, i.e., `x + 1`.
*   The resulting array is returned by the `incrList` function.

Example usage:
```
console.log(incrList([1, 2, 3])); // Output: [2, 3, 4]
console.log(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])); // Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This solution is concise and efficient, as it uses the built-in `map` function and does not require any explicit looping or indexing.