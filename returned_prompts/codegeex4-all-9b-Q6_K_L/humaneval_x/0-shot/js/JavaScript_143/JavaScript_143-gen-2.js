```js
const wordsInSentence = (sentence) => {
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  const words = sentence.split(' ');
  const primeLengthWords = words.filter(word => isPrime(word.length));
  return primeLengthWords.join(' ');
};
```