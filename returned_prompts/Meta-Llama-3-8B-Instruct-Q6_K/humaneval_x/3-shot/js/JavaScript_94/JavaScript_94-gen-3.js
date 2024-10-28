  let maxPrime = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > maxPrime) {
        maxPrime = lst[i];
      }
    }
  }
  return sumOfDigits(maxPrime);
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
}

function sumOfDigits(n) {
  return n.toString().split('').reduce((acc, curr) => parseInt(acc) + parseInt(curr), 0);
}