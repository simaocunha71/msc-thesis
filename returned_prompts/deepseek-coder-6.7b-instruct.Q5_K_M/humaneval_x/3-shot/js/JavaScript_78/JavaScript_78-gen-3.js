  const primes = new Set([2, 3, 5, 7, 11, 13]);
  let count = 0;

  for (let digit of num) {
    let decimal = parseInt(digit, 16);
    if (primes.has(decimal)) {
      count++;
    }
  }

  return count;
}



