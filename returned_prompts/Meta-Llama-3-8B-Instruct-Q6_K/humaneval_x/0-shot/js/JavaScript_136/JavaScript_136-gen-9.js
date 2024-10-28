Here is a JavaScript function that fulfills the requirements:

```javascript
const largestSmallestIntegers = (lst) => {
  let neg = null;
  let pos = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (neg === null || lst[i] > neg)) {
      neg = lst[i];
    } else if (lst[i] > 0 && (pos === null || lst[i] < pos)) {
      pos = lst[i];
    }
  }

  return neg === null && pos === null ? [null, null] : [neg, pos];
};
```

Here's how it works:

1. Initialize `neg` and `pos` to `null`.
2. Loop through each number in the list.
3. If a negative number is found and it's larger than the current `neg`, update `neg` with the current number.
4. If a positive number is found and it's smaller than the current `pos`, update `pos` with the current number.
5. If `neg` and `pos` are still `null` after the loop, return `[null, null]`. Otherwise, return the `neg` and `pos` values as an array.

You can test this function with the examples you provided:

```javascript
console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); // Output: [null, 1]
console.log(largestSmallestIntegers([])); // Output: [null, null]
console.log(largestSmallestIntegers([0])); // Output: [null, null]
```