  function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    let i = 5;
    while (i * i <= num) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
      i += 6;
    }
    return true;
  }

  let maxPrime = 0;
  for (let num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }
  return maxPrime.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
}