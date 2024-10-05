```javascript
const stringSequence = (n) => {
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim(); // remove trailing space
};
```



Test cases:

```javascript
console.log(stringSequence(0)); // '0'
console.log(stringSequence(5)); // '0 1 2 3 4 5'
```



Explanation:

- We use a `for` loop to iterate from 0 to `n` (inclusive).
- Inside the loop, we concatenate each number with a space (`' '`).
- After the loop, we use `trim()` to remove the trailing space. This ensures that the resulting string doesn't have an extra space at the end.