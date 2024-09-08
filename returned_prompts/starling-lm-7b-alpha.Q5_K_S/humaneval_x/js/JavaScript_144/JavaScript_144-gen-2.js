  let x_numerator = Number(x.split('/')[0]);
  let x_denominator = Number(x.split('/')[1]);
  let n_numerator = Number(n.split('/')[0]);
  let n_denominator = Number(n.split('/')[1]);

  let lcm = x_denominator * n_denominator;
  let new_numerator = x_numerator * (n_denominator / lcm) + n_numerator * (x_denominator / lcm);
  let new_denominator = lcm;

  if (new_numerator % new_denominator == 0) {
    return true;
  } else {
    return false;
  }
}



