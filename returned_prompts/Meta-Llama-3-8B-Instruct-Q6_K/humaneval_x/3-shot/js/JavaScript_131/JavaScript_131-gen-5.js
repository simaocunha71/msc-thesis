  let product = 1;
  let is_first_odd = true;

  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 !== 0) {
      if (is_first_odd) {
        product = digit;
        is_first_odd = false;
      } else {
        product *= digit;
      }
    }
    n = Math.floor(n / 10);
  }
  return product;
}
//OR
const digits = (n) => {
  let product = 1;
  for (let digit of n.toString().split('').map(Number)) {
    if (digit % 2 !== 0) {
      product *= digit;
    }
  }
  return product;
}