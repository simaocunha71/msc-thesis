Here is the solution:

```javascript
const stringSequence = (n) => {
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim(); // remove trailing space
};
```


Explanation:
- We initialize an empty string `result` to store the result.
- We use a for loop to iterate from 0 to `n` inclusive.
- Inside the loop, we concatenate the current number `i` to the `result` string followed by a space using the `+=` operator.
- After the loop, we use the `trim()` method to remove the trailing space from the `result` string.
- Finally, we return the `result` string.