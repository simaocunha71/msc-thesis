To solve this problem we need to break the sentence into an array of words, then filter the words by checking if their length is a prime number, finally join the selected words into a string.

Here's a step-by-step breakdown of the solution:

1. Split the sentence into an array of words using the `split` method with a space as the delimiter: `sentence.split(" ")`.
2. Check if a number is prime by using a function that checks if a number has any divisors other than 1 and itself. Here's a sample implementation of the function:

```
function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i < n; i++) {
    if (n % i === 0) return false;
  }
  return true;
}
```

3. Filter the array of words by selecting only the words whose lengths are prime numbers using the `filter` method and the `isPrime` function: `words.filter(word => isPrime(word.length))`.
4. Join the selected words into a string using the `join` method with a space as the separator: `selectedWords.join(" ")`.
5. Return the resulting string.

Here's the complete solution code:

```javascript
function wordsInSentence(sentence) {
  const words = sentence.split(" ");
  const selectedWords = words.filter(word => isPrime(word.length));
  return selectedWords.join(" ");
}
```

This solution has a time complexity of O(n), where n is the length of the sentence, as we need to iterate through each word in the sentence to check if its length is prime. The space complexity is O(n), as we need to store all the selected words in the `selectedWords` array.

Note: Make sure to define the `isPrime` function outside of the `wordsInSentence` function or in a global scope, so that it's accessible to the `wordsInSentence` function.

*/

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i