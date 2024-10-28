  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i < Math.sqrt(n); i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

  const digitSum = (n) => {
    let sum = 0;
    while (n > 0) {
      sum += n % 10;
      n = Math.floor(n / 10);
    }
    return sum;
  }

  let maxPrime = 0;
  for (const num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }

  return digitSum(maxPrime);
}