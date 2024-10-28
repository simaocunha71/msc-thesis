  let a = 0, b = 1, count = 0;
  while (count < n) {
    let temp = a + b;
    a = b;
    b = temp;
    if (isPrime(b)) {
      count++;
    }
  }
  return b;
}

const isPrime = (number) => {
  if (number < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(number); i <= sqrt; i++) {
    if (number % i === 0) return false;
  }
  return true;
};