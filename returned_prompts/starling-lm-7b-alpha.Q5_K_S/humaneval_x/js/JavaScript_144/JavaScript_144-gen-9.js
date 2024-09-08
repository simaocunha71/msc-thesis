  let x_numerator = x.split("/")[0];
  let x_denominator = x.split("/")[1];
  let n_numerator = n.split("/")[0];
  let n_denominator = n.split("/")[1];

  let x_new_numerator = x_numerator * n_denominator;
  let x_new_denominator = x_denominator * n_numerator;

  let gcd = (x_new_numerator, x_new_denominator) => {
    if (x_new_denominator == 0) return x_new_numerator;
    return gcd(x_new_denominator, x_new_numerator % x_new_denominator);
  };

  let gcd_result = gcd(x_new_numerator, x_new_denominator);

  if (gcd_result % 1.0 == 0) {
    return true;
  } else {
    return false;
  }
}



