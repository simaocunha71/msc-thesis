  let x_numerator = x.split('/')[0];
  let x_denominator = x.split('/')[1];
  let n_numerator = n.split('/')[0];
  let n_denominator = n.split('/')[1];

  let new_numerator = (x_numerator * n_denominator);
  let new_denominator = (x_denominator * n_numerator);

  let gcd = (a, b) => {
    while (b) {
      let r = a % b;
      a = b;
      b = r;
    }
    return a;
  }

  let gcd_numerator = gcd(new_numerator, new_denominator);
  new_numerator = new_numerator / gcd_numerator;
  new_denominator = new_denominator / gcd_numerator;

  if (new_numerator * new_denominator == Math.round(new_numerator * new_denominator)) {
    return true;
  } else {
    return false;
  }
}



