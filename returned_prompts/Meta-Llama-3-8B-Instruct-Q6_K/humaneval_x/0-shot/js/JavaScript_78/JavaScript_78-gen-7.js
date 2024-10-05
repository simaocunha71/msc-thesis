Here is the solution to the problem:

```javascript
const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    const digit = num[i];
    if (digit === '2' || digit === '3' || digit === '5' || digit === '7' || digit === 'B' || digit === 'D') {
      count++;
    }
  }
  return count;
};
```
This function iterates over each character in the input string. If the character is a prime hexadecimal digit (2, 3, 5, 7, B, or D), it increments a counter. Finally, it returns the count of prime hexadecimal digits.

Note: This solution assumes that the input string is always correct or empty. It also assumes that the input string only contains uppercase hexadecimal digits. If the input string can contain lowercase letters or other characters, additional error checking may be necessary.