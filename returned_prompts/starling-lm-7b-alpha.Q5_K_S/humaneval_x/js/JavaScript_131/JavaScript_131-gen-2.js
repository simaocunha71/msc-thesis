  let product = 1;
  let is_odd = false;

  while (n > 0) {
    let last_digit = n % 10;
    if (last_digit % 2 != 0) {
      if (!is_odd) {
        product = last_digit;
        is_odd = true;
      } else {
        product *= last_digit;
      }
    }
    n = Math.floor(n / 10);
  }

  return product;
}



