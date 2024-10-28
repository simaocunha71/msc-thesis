To solve this problem, we'll need to do the following steps:

1. Split the sentence into words using the `split` method.
2. Check if the length of each word is a prime number.
3. Create a new string with the words whose lengths are prime numbers.
4. Return the new string.

Here's the solution:

```javascript
const wordsInSentence = (sentence) => {
  // Helper function to check if a number is prime
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  // Split the sentence into words
  const words = sentence.split(' ');

  // Filter the words whose lengths are prime numbers
  const primeLengthWords = words.filter(word => isPrime(word.length));

  // Join the filtered words back into a string
  return primeLengthWords.join(' ');
};
```

Let's test the function with the provided examples:

```javascript
console.log(wordsInSentence("This is a test")); // Output: "is"
console.log(wordsInSentence("lets go for swimming")); // Output: "go for"
```

The function should return the expected outputs.