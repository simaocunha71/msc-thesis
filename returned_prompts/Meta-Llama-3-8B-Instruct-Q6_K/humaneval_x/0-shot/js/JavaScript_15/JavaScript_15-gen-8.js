```javascript
const stringSequence = (n) => {
  return Array(n + 1).fill(0).map((_, i) => i).join(' ');
};
```


Explanation:
We use the `Array.fill()` method to create an array of length `n + 1` filled with zeros. We then use the `map()` method to create a new array where each element is the index of the corresponding element in the original array (starting from 0). Finally, we use the `join()` method to concatenate the elements of the array into a string, with spaces separating each number. The resulting string is the desired sequence of space-delimited numbers.