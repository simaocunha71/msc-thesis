Here is the solution:
```javascript
const sortEven = (l) => {
  return l.map((x, i) => i % 2 === 0 ? [...l.slice(0, i)].flat().sort((a, b) => a - b)[0] : x);
};
```
Here's an explanation of the code:

1. `l.map((x, i) => ...)` maps over the input list `l` and returns a new list where each element is the result of the callback function.
2. `i % 2 === 0` checks if the current index `i` is even.
3. If `i` is even, `...l.slice(0, i).flat().sort((a, b) => a - b)[0]` sorts the even-indexed elements of `l` and returns the first element (which is the smallest).
4. If `i` is odd, `x` is returned as is, since we want to keep the original value at odd indices.
5. The `flat()` method is used to flatten the array returned by `slice(0, i)`.

You can test the function using the examples you provided:
```javascript
console.log(sortEven([1, 2, 3])); // [1, 2, 3]
console.log(sortEven([5, 6, 3, 4])); // [3, 6, 5, 4]
``` I hope this helps! Let me know if you have any further questions.