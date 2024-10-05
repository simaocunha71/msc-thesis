  let x_numerator = parseInt(x.split('/')[0]);
  let x_denominator = parseInt(x.split('/')[1]);
  let n_numerator = parseInt(n.split('/')[0]);
  let n_denominator = parseInt(n.split('/')[1]);

  let product_numerator = x_numerator * n_numerator;
  let product_denominator = x_denominator * n_denominator;

  let gcd = (a, b) => {
    if (b == 0) {
      return a;
    }
    return gcd(b, a % b);
  }

  let common_divisor = gcd(product_numerator, product_denominator);

  product_numerator /= common_divisor;
  product_denominator /= common_divisor;

  if (product_denominator == 1) {
    return true;
  }
  return false;
}