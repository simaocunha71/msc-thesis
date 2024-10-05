  var primes = ['2', '3', '5', '7', 'B', 'D'];
  var count = 0;
  for (const c of num) {
    if (primes.includes(c)) {
      count += 1;
    }
  }
  return count;
}