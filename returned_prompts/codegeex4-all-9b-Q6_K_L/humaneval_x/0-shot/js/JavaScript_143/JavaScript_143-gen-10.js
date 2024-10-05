To solve this problem, we will follow these steps:

1. Create a helper function to check if a number is prime.
2. Split the sentence into an array of words.
3. Filter the array of words to only include words whose lengths are prime numbers.
4. Join the filtered array of words back into a string.
5. Return the resulting string.

Here is the implementation of the `wordsInSentence` function in JavaScript:

```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const primeWords = words.filter(word => isPrime(word.length));
  return primeWords.join(' ');
};
```

This function first checks if a number is prime using the helper function `isPrime`. Then, it splits the sentence into an array of words using the `split` method. It filters the array of words to only include words whose lengths are prime numbers using the `filter` method and the `isPrime` helper function. Finally, it joins the filtered array of words back into a string using the `join` method and returns the resulting string.