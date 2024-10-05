  let maxPrime = 0;

  for (const num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }

  return sumOfDigits(maxPrime);
}

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

const sumOfDigits = (num) => {
  let sum = 0;
  while (num > 0) {
    sum += num % 10;
    num = Math.floor(num / 10);
  }
  return sum;
}



