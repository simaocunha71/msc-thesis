Here is a possible implementation of the function:
```
const hexKey = (num) => {
  const hexDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    const digit = hexDigits.indexOf(num[i]);
    if (digit >= 2 && isPrime(digit + 2)) {
      count++;
    }
  }
  return count;
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```
Here's an explanation of how the function works:

1. We define an array `hexDigits` that contains the hexadecimal digits.
2. We initialize a variable `count` to 0, which will keep track of the number of prime hexadecimal digits.
3. We iterate over each character `num[i]` in the input string `num`.
4. For each character, we find its corresponding index in the `hexDigits` array using `indexOf`. If the index is greater than or equal to 2, it means the character is a hexadecimal digit (not 0 or 1).
5. We check if the index (plus 2) is a prime number using the `isPrime` function. If it is, we increment the `count` variable.
6. Finally, we return the `count` variable, which represents the number of prime hexadecimal digits in the input string.

The `isPrime` function is a simple implementation of the Sieve of Eratosthenes algorithm, which checks if a number is prime by iterating from 2 to the square root of the number and checking if it has any divisors. If it does, it returns `false`, otherwise it returns `true`. This function is used to check if a hexadecimal digit (plus 2) is a prime number.

Note that this implementation assumes that the input string only contains valid hexadecimal digits (0-9, A-F). If the input string contains invalid characters, the function may not work correctly. You may want to add error handling to handle such cases.