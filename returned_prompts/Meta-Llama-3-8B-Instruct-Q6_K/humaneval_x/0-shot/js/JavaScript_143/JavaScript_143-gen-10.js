```
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  return words.filter(word => {
    const num = parseInt(word);
    if (num > 1 && isPrime(num)) {
      return true;
    }
    return false;
  }).join(' ');
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```

This code splits the input sentence into words using the `split` method, then filters the words using the `filter` method. The filtering function checks if the length of each word is a prime number using the `isPrime` helper function. If the length is a prime number, the word is included in the filtered array. Finally, the filtered array is joined back into a string using the `join` method.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the iterated values. If it is, the function returns `false`, indicating that the number is not prime. If the loop completes without finding a divisor, the function returns `true`, indicating that the number is prime.