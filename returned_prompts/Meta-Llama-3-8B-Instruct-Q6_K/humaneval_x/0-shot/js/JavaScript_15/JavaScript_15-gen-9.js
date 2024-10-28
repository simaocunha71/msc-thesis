```javascript
const stringSequence = (n) => {
  return Array(n + 1).fill(0).map((_, index) => index.toString()).join(' ');
};
```


Explanation:
This function uses the `Array` constructor to create an array of `n+1` elements, all initialized to 0. The `map` method is used to transform each element to a string, and the `_` variable is used to ignore the element value. The `join` method is then used to concatenate the array elements with a space character in between. The resulting string is the space-delimited sequence of numbers from 0 to `n` inclusive.