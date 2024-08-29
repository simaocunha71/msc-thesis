  let result = 1;
  let isOdd = false;

  while (n != 0) {
    let digit = n % 10;
    if (digit % 2 != 0) {
      if (isOdd) {
        result *= digit;
      } else {
        result = digit;
        isOdd = true;
      }
    }
    n = Math.floor(n / 10);
  }
  return result;
}



