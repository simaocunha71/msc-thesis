  const primes = new Set(['2', '3', '5', '7', 'B', 'D']);
  let count = 0;
  for (let c of num) {
    if (primes.has(c)) {
      count++;
    }
  }
  return count;
}



