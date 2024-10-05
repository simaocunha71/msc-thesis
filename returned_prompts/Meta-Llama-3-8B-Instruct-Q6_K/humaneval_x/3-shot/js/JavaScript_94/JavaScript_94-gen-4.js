  let maxPrime = -1;
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > maxPrime) {
        maxPrime = lst[i];
      }
    }
  }
  if (maxPrime > 0) {
    sum = sumDigits(maxPrime);
  }
  return sum;
}

function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if (num % i === 0) return false;
  return true;
}

function sumDigits(num) {
  return num.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
}