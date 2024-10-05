```javascript
const stringSequence = (n) => {
  return Array(n + 1).join(' ').split(',').slice(1, -1).join(' ');
};
```
Explanation:
The function `stringSequence` takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` inclusive.

We use the `Array` constructor to create an array of length `n + 1` filled with zeros. The `join(' ')` method is used to concatenate the elements of the array into a string with spaces in between.

The resulting string is then split into an array using the `split(',')` method, which separates the string into an array of substrings using commas as the separator. We then use the `slice(1, -1)` method to remove the first and last elements of the array (which are empty strings), leaving us with an array of numbers.

Finally, we use the `join(' ')` method again to concatenate the elements of the array into a string with spaces in between, and return the resulting string.