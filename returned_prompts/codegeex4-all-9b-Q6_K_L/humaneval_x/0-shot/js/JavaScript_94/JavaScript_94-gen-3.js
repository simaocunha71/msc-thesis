```java
const skjkasdkd = (lst) => {
  let largestPrime = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > largestPrime && isPrime(lst[i])) {
      largestPrime = lst[i];
    }
  }
  return sumDigits(largestPrime);
}

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

const sumDigits = (num) => {
  return num.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
}
```
