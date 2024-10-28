```js
const skjkasdkd = (lst) => {
  let maxPrime = 0;
  for (let num of lst) {
    if (num > maxPrime && isPrime(num)) {
      maxPrime = num;
    }
  }
  return sumDigits(maxPrime);
};

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const sumDigits = (num) => {
  return num.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
};
```
