  let odd_product = 1;
  for (let digit of n.toString()) {
    if (digit % 2 == 1) {
      odd_product *= digit;
    }
  }
  return odd_product;
}