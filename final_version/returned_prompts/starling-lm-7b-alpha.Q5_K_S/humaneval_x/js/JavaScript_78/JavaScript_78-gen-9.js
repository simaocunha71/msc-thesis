  let decimal_str = '';
  for (const digit of hex_str) {
    decimal_str += hexToDecimal(digit).toString();
  }

  let primes_count = 0;
  for (const digit of decimal_str) {
    if (isPrime(parseInt(digit))) {
      primes_count += 1;
    }
  }
  return primes_count;
}



