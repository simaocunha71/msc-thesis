  var max_prime = 0;
  for (const num of lst) {
    if (num > max_prime && isPrime(num)) {
      max_prime = num;
    }
  }
  return String(max_prime).split('').reduce((a, b) => a + Number(b), 0);
}