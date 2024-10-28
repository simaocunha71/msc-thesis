  var primes = [2, 3, 5, 7];
  var count = 0;
  for (const c of num) {
    var digit = parseInt(c, 16);
    if (primes.includes(digit)) {
      count += 1;
    }
  }
  return count;
}