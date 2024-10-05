```js
const isPrime = (num) => {
  if (num <= 1) return false;
  if (num <= 3) return true;

  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }

  return true;
};

const skjkasdkd = (lst) => {
  let maxPrime = -1;

  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i]) && lst[i] > maxPrime) {
      maxPrime = lst[i];
    }
  }

  let sumOfDigits = 0;
  while (maxPrime > 0) {
    sumOfDigits += maxPrime % 10;
    maxPrime = Math.floor(maxPrime / 10);
  }

  return sumOfDigits;
};
```