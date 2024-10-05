```java
const wordsInSentence = (sentence) => {
  let arr = sentence.split(" ")
  let isPrime = (num) => {
    if (num < 2) return false
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false
    }
    return true
  }
  let result = arr.filter((word) => isPrime(word.length))
  return result.join(" ")
}
```
