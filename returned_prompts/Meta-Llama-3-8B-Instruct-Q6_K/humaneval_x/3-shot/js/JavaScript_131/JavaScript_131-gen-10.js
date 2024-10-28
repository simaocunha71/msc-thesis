  let product = 1;
  let oddFound = false;

  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 != 0) {
      product *= digit;
      oddFound = true;
    }
    n = Math.floor(n / 10);
  }

  return oddFound ? product : 0;
}