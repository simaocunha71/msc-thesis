```
function wordsInSentence(sentence) {
  let words = sentence.split(' ');
  let result = '';
  for (let word of words) {
    let isPrime = true;
    for (let i = 2, sqrt = Math.sqrt(word.length); i <= sqrt; i++) {
      if (word.length % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      result += word + ' ';
    }
  }
  return result.trim();
}
```
This function splits the input sentence into words and then iterates over each word. For each word, it checks if the length of the word is a prime number by iterating from 2 to the square root of the word length and checking if the word length is divisible by any of these numbers. If the word length is a prime number, it adds the word to the result string. Finally, it returns the result string after trimming any trailing spaces.