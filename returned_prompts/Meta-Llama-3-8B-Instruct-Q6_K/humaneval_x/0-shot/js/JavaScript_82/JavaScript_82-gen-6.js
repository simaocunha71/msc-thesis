```
function primeLength(str) {
  let len = str.length;
  if (len <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(len); i <= sqrt; i++) {
    if (len % i === 0) return false;
  }
  return true;
}
```
Explanation:
This function calculates the length of the input string and checks if it's a prime number. It uses a for loop to iterate from 2 to the square root of the length (since a larger factor of the number would be a multiple of smaller factor that has already been checked). If the length is divisible by any of these numbers, it's not a prime number and the function returns false. If the length is prime, the function returns true.

The examples given in the problem statement are:
- "Hello" with a length of 5, which is a prime number
- "abcdcba" with a length of 8, which is also a prime number
- "kittens" with a length of 7, which is a prime number
- "orange" with a length of 6, which is not a prime number

The function correctly returns true for the first three examples and false for the last one.