To solve this problem, you need to first split the sentence into words. Then, check the length of each word. If the length is a prime number, add the word to the result. Finally, join the words with a space and return the result.

Here is the complete code:

```javascript
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const primes = [];
  
  for (let i = 0; i < words.length; i++) {
    if (isPrime(words[i].length)) {
      primes.push(words[i]);
    }
  }
  
  return primes.join(' ');
};

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  
  return true;
};

console.log(wordsInSentence("This is a test")); // Output: "is"
console.log(wordsInSentence("lets go for swimming")); // Output: "go for"
```

This code defines two functions: `wordsInSentence` and `isPrime`. `wordsInSentence` takes a sentence as input and returns a string containing the words whose lengths are prime numbers. `isPrime` is a helper function that checks if a number is prime or not.