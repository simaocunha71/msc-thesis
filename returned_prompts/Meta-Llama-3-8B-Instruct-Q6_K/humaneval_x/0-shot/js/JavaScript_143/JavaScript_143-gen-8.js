```
function wordsInSentence(sentence) {
  const words = sentence.split(' ');
  const result = [];
  
  for (const word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }
  
  return result.join(' ');
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}

console.log(wordsInSentence("This is a test")); // Output: "is"
console.log(wordsInSentence("lets go for swimming")); // Output: "go for"
```

Explanation:
The function `wordsInSentence` splits the input sentence into individual words using the `split` method. Then it iterates over the words and checks if the length of each word is a prime number using the `isPrime` function. If the length of a word is a prime number, it adds the word to the result array. Finally, it joins the words in the result array with a space character using the `join` method and returns the resulting string.

The `isPrime` function checks if a given number `n` is prime. It does this by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible, it returns `false`, indicating that `n` is not a prime number. If `n` is not divisible by any of these numbers, it returns `true`, indicating that `n` is a prime number.