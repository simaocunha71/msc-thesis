```
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const primeWords = words.filter((word) => {
    const isPrime = (n) => {
      if (n <= 1) return false;
      for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) return false;
      }
      return true;
    };
    return isPrime(word.length);
  });
  return primeWords.join(' ');
};
```
The above function takes a sentence as input, splits it into words, and then filters out the words whose lengths are not prime numbers. Finally, it joins the remaining words back into a string with spaces in between.

The `isPrime` function is a helper function that checks if a given number is prime. It does this by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of these values, the function returns `true`, indicating that the number is prime.

The `filter` method is used to apply the `isPrime` function to each word in the sentence and return a new array containing only the words whose lengths are prime numbers. The `join` method is then used to concatenate these words back into a string with spaces in between.