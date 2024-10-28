Here is the solution to the problem:
```javascript
const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hexDigit = num[i];
    if (hexDigit === '2' || hexDigit === '3' || hexDigit === '5' || hexDigit === '7' || hexDigit === 'B' || hexDigit === 'D') {
      count++;
    }
  }
  return count;
};
```
This function iterates over each character in the input string `num`. It checks if the character is a prime hexadecimal digit (2, 3, 5, 7, B, or D). If it is, it increments the `count` variable. Finally, it returns the `count` variable.

You can test this function with the examples provided in the problem statement:
```javascript
console.log(hexKey("AB")); // Output: 1
console.log(hexKey("1077E")); // Output: 2
console.log(hexKey("ABED1A33")); // Output: 4
console.log(hexKey("123456789ABCDEF0")); // Output: 6
console.log(hexKey("2020")); // Output: 2
```
I hope this helps! Let me know if you have any questions. 😊

Note: This solution assumes that the input string `num` is always a valid hexadecimal number. If the input string can be invalid, you may want to add error handling to handle such cases. For example, you could use a regular expression to validate the input string.