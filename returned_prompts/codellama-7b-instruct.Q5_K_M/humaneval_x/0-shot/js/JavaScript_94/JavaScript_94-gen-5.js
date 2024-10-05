const skjkasdkd = (lst) => {

function getLargestPrime(lst) {
  let largestPrime;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (!largestPrime || lst[i] > largestPrime) {
        largestPrime = lst[i];
      }
    }
  }
  return largestPrime;
}

function isPrime(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function sumDigits(n) {
  return n.toString().split('').map(x => +x).reduce((a, b) => a + b, 0);
}

const largestPrime = getLargestPrime(lst);
console.log(largestPrime);
return sumDigits(largestPrime);
}

skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]);
skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]);
skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]);
skjkasdkd([0, 724, 32, 71, 99