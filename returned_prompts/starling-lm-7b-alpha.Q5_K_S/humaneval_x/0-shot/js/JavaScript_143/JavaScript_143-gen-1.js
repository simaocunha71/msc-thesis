Here is my solution:

```javascript
function wordsInSentence(sentence) {
  const words = sentence.split(" ");
  const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317];
  const primesLengths = primes.map(prime => prime.toString());
  const validWords = words.filter(word => primesLengths.includes(word.length.toString()));
  return validWords.join(" ");
}
```

This solution first splits the sentence into an array of words, then creates an array of prime numbers up to the maximum possible length of a word in the sentence. It then maps the prime numbers to their string representations. It filters the words array to only include words of length that are in the primesLengths array. Finally, it joins the valid words back into a sentence with spaces between them.

The time complexity of this solution is O(n), where n is the number of words in the sentence, as each word is checked only