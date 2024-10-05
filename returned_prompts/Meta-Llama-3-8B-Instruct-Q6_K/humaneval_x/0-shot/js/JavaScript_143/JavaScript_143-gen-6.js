```javascript
function wordsInSentence(sentence) {
  let words = sentence.split(' ');
  let result = '';

  for (let word of words) {
    if (isPrime(word.length)) {
      result += word + ' ';
    }
  }

  return result.trim();
}

function isPrime(n) {
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;

  let max = Math.floor(Math.sqrt(n));
  for (let i = 3; i <= max; i += 2) {
    if (n % i === 0) return false;
  }

  return true;
}
```
The above code splits the sentence into words and then iterates over each word to check if its length is a prime number. If it is, the word is added to the result string. The `isPrime` function checks if a number is prime by iterating over possible divisors up to the square root of the number and returning false if any divisor is found. Finally, the `wordsInSentence` function returns the result string trimmed to remove any trailing spaces.