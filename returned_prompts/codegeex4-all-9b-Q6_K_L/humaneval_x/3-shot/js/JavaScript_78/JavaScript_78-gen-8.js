  let count = 0;
  let primes = ['2', '3', '5', '7', 'B', 'D'];
  for (const digit of num) {
    if (primes.includes(digit)) {
      count += 1;
    }
  }
  return count;
}