  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hexDigit = num[i];
    let decimalValue = parseInt(hexDigit, 16);
    if (isPrime(decimalValue)) {
      count++;
    }
  }
  return count;

  function isPrime(n) {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }
}