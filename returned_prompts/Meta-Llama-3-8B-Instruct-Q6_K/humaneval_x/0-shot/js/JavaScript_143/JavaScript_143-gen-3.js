```
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const result = [];

  for (const word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }

  return result.join(' ');
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```
This solution works by first splitting the input sentence into words. Then, it iterates over each word, checking if its length is a prime number using the `isPrime` function. If it is, the word is added to the result array. Finally, the result array is joined back into a string with spaces in between, and returned.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number, and checking if the number is divisible by any of the values. If it is, the function returns `false`, indicating that the number is not prime. If the function reaches the end without finding a divisor, it returns `true`, indicating that the number is prime.