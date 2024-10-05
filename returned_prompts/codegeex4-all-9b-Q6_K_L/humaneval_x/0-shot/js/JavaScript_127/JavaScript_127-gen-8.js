```js
const intersection = (interval1, interval2) => {
  const [start1, end1] = interval1
  const [start2, end2] = interval2
  const start = Math.max(start1, start2)
  const end = Math.min(end1, end2)
  const length = end - start + 1
  const isPrime = (num) => {
    if (num <= 1) return false
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false
    }
    return true
  }
  return isPrime(length) ? "YES" : "NO"
}
```