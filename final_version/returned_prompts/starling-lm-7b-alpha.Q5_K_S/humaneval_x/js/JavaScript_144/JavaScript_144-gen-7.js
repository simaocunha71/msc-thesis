  let x_numerator = +x.split('/')[0];
  let x_denominator = +x.split('/')[1];
  let n_numerator = +n.split('/')[0];
  let n_denominator = +n.split('/')[1];

  let lcm = (n_denominator * x_denominator) / gcd(n_denominator, x_denominator);
  let new_numerator = lcm / x_denominator * n_numerator;
  let new_denominator = lcm / x_denominator;

  if (new_numerator % 1 === 0) {
    return true;
  } else {
    return false;
  }
}

function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}



