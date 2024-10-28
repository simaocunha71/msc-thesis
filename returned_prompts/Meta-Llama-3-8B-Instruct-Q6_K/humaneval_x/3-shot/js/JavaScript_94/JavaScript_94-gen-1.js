  let maxPrime = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      maxPrime = lst[i];
      break;
    }
  }
  return sumDigits(maxPrime);
}

function isPrime(n) {
  if (n < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
    if (n % i === 0) return false;
  return true;
}

function sumDigits(n) {
  return n.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
}