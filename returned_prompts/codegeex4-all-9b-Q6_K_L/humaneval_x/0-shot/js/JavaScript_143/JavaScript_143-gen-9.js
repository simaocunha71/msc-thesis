To solve this problem, we can use the following steps:

1. Split the sentence into an array of words using the `split` method.
2. Create an empty string to store the words with prime lengths.
3. Iterate over the array of words.
4. For each word, check if its length is a prime number.
5. If the length is a prime number, add the word to the string from step 3.
6. Return the string from step 3.

Here is the complete code:

```javascript
const wordsInSentence = (sentence) => {
  const words = sentence.split(" ");
  const primeLengthWords = "";

  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    const length = word.length;

    if (isPrime(length)) {
      primeLengthWords += word + " ";
    }
  }

  return primeLengthWords.trim();
};

const isPrime = (num) => {
  if (num <= 1) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
};
```

This code defines a function `wordsInSentence` that takes a sentence as input and returns a string that contains the words from the original sentence, whose lengths are prime numbers. The `isPrime` function is used to check if a number is prime or not. The `split` method is used to split the sentence into an array of words, and the `trim` method is used to remove any extra spaces from the resulting string.