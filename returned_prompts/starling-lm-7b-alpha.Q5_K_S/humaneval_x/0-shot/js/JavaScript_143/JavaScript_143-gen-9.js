To solve this problem, we can follow these steps:

1. Split the sentence into an array of words.
2. Filter the array to keep only the words with lengths that are prime numbers.
3. Join the filtered array back into a string.
4. Return the resulting string.

Here's a step-by-step breakdown of the solution:

1. We start by splitting the input sentence into an array of words using the `split()` method. This method splits the sentence based on spaces, so each word will be a separate element in the array.

2. Next, we filter the array to keep only the words with lengths that are prime numbers. We can do this by iterating over the array and checking if the length of each word is a prime number. We can use the `isPrime()` helper function to determine if a number is prime. This function takes an integer as input and returns `true` if the number is prime, and `false` otherwise. Here's the implementation of the `isPrime()` function:

```javascript
function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
```

3. After filtering the array, we join the remaining words back into a string using the `join()` method. This method takes a separator as an optional parameter, and by default, it uses a space as the separator. Since we want to keep the original order of the words in the sentence, we don't need to provide a separator.

4. Finally, we return the resulting string.

Here's the complete solution in code:

```javascript
function wordsInSentence(sentence) {
  const words = sentence.split(' ');
  const filteredWords = words.filter(word => isPrime(word.length));
  return filteredWords.join(' ');
}
```

This solution has a time complexity of O(n), where n is the length of the sentence, as we iterate over the sentence twice. The space complexity is O(1), as we only use a constant amount of additional space