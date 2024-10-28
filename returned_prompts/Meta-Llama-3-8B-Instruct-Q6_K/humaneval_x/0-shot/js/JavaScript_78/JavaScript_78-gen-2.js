Here is a JavaScript function that counts the number of hexadecimal digits that are primes:
```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};

const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    const digit = num[i];
    if (digit >= '2' && digit <= '7') {
      if (isPrime(parseInt(digit, 10))) {
        count++;
      }
    } else if (digit === 'B' || digit === 'D') {
      count++;
    }
  }
  return count;
};
```
The function `isPrime` checks if a given number is prime. The function `hexKey` iterates over each character in the input string `num`. If the character is a hexadecimal digit from 2 to 7, it checks if the corresponding decimal number is prime using the `isPrime` function. If it is, it increments the `count` variable. If the character is 'B' or 'D', it also increments the `count` variable because these digits represent prime numbers in hexadecimal. Finally, the function returns the total count.

You can test the function with the examples provided:
```javascript
console.log(hexKey("AB")); // 1
console.log(hexKey("1077E")); // 2
console.log(hexKey("ABED1A33")); // 4
console.log(hexKey("123456789ABCDEF0")); // 6
console.log(hexKey("2020")); // 2
```
Note that the function assumes that the input string only contains uppercase hexadecimal digits and does not contain any whitespace or other characters. If the input string can contain other characters, you may need to add additional error handling.