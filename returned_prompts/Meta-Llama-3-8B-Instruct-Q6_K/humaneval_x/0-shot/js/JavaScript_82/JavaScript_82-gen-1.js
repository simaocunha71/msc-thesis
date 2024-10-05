The function primeLength checks if the length of the input string is a prime number. Here's how you can do it:

```
const primeLength = (string) => {
  const length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};
```


In this function, we first check if the length of the string is less than or equal to 1. If it is, we return false because 0 and 1 are not prime numbers.

Then, we use a for loop to check if the length of the string is divisible by any number from 2 to the square root of the length. If it is, we return false because the length is not a prime number.

If the length is not divisible by any of these numbers, we return true because the length is a prime number.

This function works for strings of any length, not just the examples provided. It will correctly identify prime lengths in strings like "Hello", "abcdcba", "kittens", and "orange". For example, primeLength('Hello') will return true because the length of the string "Hello" is 5, which is a prime number. On the other hand, primeLength('orange') will return false because the length of the string "orange" is 6, which is not a prime number.