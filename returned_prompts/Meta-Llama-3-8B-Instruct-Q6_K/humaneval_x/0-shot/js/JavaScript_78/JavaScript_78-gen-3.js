Here is the solution:
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
Explanation:

* We initialize a variable `count` to keep track of the number of prime hexadecimal digits.
* We iterate through each character `hexDigit` in the input string `num`.
* We check if the hexadecimal digit is a prime digit (2, 3, 5, 7, B, or D).
* If it is, we increment the `count` variable.
* Finally, we return the `count` variable.

Testing:
```javascript
console.log(hexKey("AB")); // 1
console.log(hexKey("1077E")); // 2
console.log(hexKey("ABED1A33")); //