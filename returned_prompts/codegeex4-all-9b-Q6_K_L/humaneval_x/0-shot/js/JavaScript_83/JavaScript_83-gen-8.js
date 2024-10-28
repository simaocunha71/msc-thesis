The question asks to count the numbers of n-digit positive integers that start or end with 1. This means that the first digit can be 1 and the last digit can be 1.

For example, if n = 2, the numbers that start or end with 1 are:

11
21
12
The answer would be 4.

Here is a possible implementation in JavaScript:

```javascript
const startsOneEnds = (n) => {
  let count = 0;
  for (let i = 1; i <= 9; i++) {
    for (let j = 1; j <= 9; j++) {
      if (i === 1 || j === 1) {
        count++;
      }
    }
  }
  return count;
}
```

This implementation iterates through all the possible first and last digits (1 to 9) and checks if either of them is 1. If so, it increments the count. Finally, it returns the count.