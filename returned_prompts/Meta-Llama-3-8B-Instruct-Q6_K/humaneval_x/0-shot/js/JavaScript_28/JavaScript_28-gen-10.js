```javascript
const concatenate = (strings = []) => strings.reduce((acc, curr) => acc + curr, '');
```



Explanation:

*   The `concatenate` function takes an array of strings as an argument.
*   The `reduce` method is used to concatenate the strings in the array.
*   The initial value of the accumulator `acc` is an empty string `''`.
*   For each string `curr` in the array, the accumulator `acc` is updated by concatenating `acc` with `curr`.
*   The resulting concatenated string is returned by the `concatenate` function.

Example usage:
```javascript
console.log(concatenate([])); // Output: ''
console.log(concatenate(['a', 'b', 'c'])); // Output: 'abc'
```



The provided solution is concise and efficient, and it correctly handles the edge case where the input array is empty. The `reduce` method is a good choice for this problem because it allows us to iterate over the array and accumulate the result in a single pass. The initial value of the accumulator ensures that the function works correctly even when the input array is empty.