```java
const skjkasdkd = (lst) => {
  var largest = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > largest && isPrime(lst[i])) {
      largest = lst[i];
    }
  }
  return sumDigits(largest);
}

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function sumDigits(num) {
  return num.toString().split('').reduce((acc, curr) => acc + Number(curr), 0);
}
```
