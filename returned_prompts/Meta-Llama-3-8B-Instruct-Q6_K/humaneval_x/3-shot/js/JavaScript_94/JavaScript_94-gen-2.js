  let maxPrime = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > maxPrime) {
        maxPrime = lst[i];
      }
    }
  }
  if (maxPrime === 0) {
    return 0;
  }
  return sumDigits(maxPrime);
}

function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function sumDigits(num) {
  let sum = 0;
  while (num > 0) {
    sum += num % 10;
    num = Math.floor(num / 10);
  }
  return sum;
}