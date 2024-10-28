  let product = 1;

  for (let i = 0; i < n.toString().length; i++) {
    let digit = parseInt(n.toString()[i]);
    if (digit % 2 != 0) {
      product *= digit;
    }
  }

  return product;
}



