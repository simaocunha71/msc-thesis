Here's one possible solution:

```javascript
const search = (lst) => {
  let freqs = {};
  for (let i = 0; i < lst.length; i++) {
    if (!(lst[i] in freqs)) {
      freqs[lst[i]] = 0;
    }
    freqs[lst[i]]++;
  }
  for (let i = Math.max(...freqs); i >= 1; i--) {
    if (freqs[i] >= i) {
      return i;
    }
  }
  return -1;
};
```

Explanation:

- We start by initializing an empty object `freqs` to keep track of the frequency of each number in the list.
- We then iterate over the input list and increment the frequency of each number in `freqs`.
- Next, we initialize a variable `i` to the maximum frequency we found in `freqs`, and decrement it until we find a number whose frequency is greater than or equal to its value, or until we reach 1.
- If we find such a number, we return it as the result. Otherwise, if we reach 1 without finding a suitable number, we return -1 as the result.

This solution has a time complexity of O(n + k), where n is the length of the input list and k is the maximum frequency found.

Note: The `Math.max(...freqs)` syntax is used to find the maximum value in the `freqs` object. The spread syntax `...` is used to spread the object's entries into an array, which can then be passed as arguments to the `Math.max` function.

I hope this helps! Let me know if you have any more questions.

Here are some additional resources for further reading on this topic:

- [Finding the Maximum Value in an Object](https://stackoverflow.com/questions/16868904/finding-the-maximum-value-in-an-object)
- [Spread Syntax in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_sy