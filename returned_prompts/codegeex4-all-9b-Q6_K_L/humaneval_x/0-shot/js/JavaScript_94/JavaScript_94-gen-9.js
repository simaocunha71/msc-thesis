```java
const skjkasdkd = (lst) => {
  let maxPrime = 0
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > maxPrime && isPrime(lst[i])) {
      maxPrime = lst[i]
    }
  }
  return sumDigits(maxPrime)
}

const isPrime = (num) => {
  if (num <= 1) return false
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false
  }
  return true
}

const sumDigits = (num) => {
  return num.toString().split('').reduce((a, b) => a + parseInt(b), 0)
}
```
