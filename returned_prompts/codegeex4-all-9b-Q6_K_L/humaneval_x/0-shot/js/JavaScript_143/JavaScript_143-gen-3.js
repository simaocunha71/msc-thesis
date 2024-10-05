```js
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ')
  const isPrime = (num) => {
    if (num <= 1) return false
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false
    }
    return true
  }
  return words.filter(word => isPrime(word.length)).join(' ')
}
```
