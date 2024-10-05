  const primes = new Set([2, 3, 5, 7, 11, 13]);
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hexDigit = parseInt(num[i], 16);
    if (primes.has(hexDigit)) {
      count++;
    }
  }
  return count;
}



