Here is the solution:
```
const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    const hexDigit = num[i];
    if (hexDigit === '2' || hexDigit === '3' || hexDigit === '5' || hexDigit === '7' || hexDigit === 'B' || hexDigit === 'D') {
      count++;
    }
  }
  return count;
};
```
Explanation:
The function `hexKey` takes a hexadecimal number as a string `num` and returns the count of hexadecimal digits that are prime.

It uses a for loop to iterate over each character `hexDigit` in the input string `num`. For each character, it checks if it is one of the prime hexadecimal digits ('2', '3', '5', '7', 'B', or 'D'). If it is, it increments a counter `count`.

Finally, the function returns the count of prime hexadecimal digits.

Examples:
```
console.log(hexKey("AB")); // Output: 1
console.log(hexKey("1077E")); // Output: 2
console.log(hexKey("ABED1A33")); // Output: 4
console.log(hexKey("123456789ABCDEF0")); // Output: 6
console.log(hexKey("2020")); // Output: 2
``` 