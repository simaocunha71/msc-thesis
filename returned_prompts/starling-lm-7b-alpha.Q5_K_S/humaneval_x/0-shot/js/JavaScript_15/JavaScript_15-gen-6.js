
To solve this problem, you can use a for loop to iterate through the numbers from 0 to `n` (inclusive) and concatenate each number with a space to the result string. Here's the implementation of the function:

```javascript
const stringSequence = (n) => {
  let result = "";
  for (let i = 0; i <= n; i++) {
