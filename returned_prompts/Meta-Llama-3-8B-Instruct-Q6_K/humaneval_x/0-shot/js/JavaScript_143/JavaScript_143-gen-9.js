```
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  return words.filter(word => isPrime(word.length)).join(' ');
};

const isPrime = num => {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
The function `wordsInSentence` takes a sentence as an input and returns a string containing the words whose lengths are prime numbers. It splits the sentence into words and filters out the words that have prime lengths using the `isPrime` function. The filtered words are then joined back into a string and returned.

The `isPrime` function checks if a given number is prime. It returns `false` if the number is less than or equal to 1, and then checks if the number has any divisors other than 1 and itself. If it finds any divisors, it returns `false`, otherwise, it returns `true`. This function is used to filter out the words with non-prime lengths.

This solution has a time complexity of O(n), where n is the number of words in the sentence, since it iterates over each word once. The space complexity is O(n) as well, since it stores the filtered words in memory.