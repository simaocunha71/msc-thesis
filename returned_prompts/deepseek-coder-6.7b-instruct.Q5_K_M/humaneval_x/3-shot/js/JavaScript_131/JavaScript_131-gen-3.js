  let product = 1;
  let hasOdd = false;

  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 != 0) {
      product *= digit;
      hasOdd = true;
    }
    n = Math.floor(n / 10);
  }

  return hasOdd ? product : 0;
}



