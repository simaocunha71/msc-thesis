  let x_numerator = parseInt(x.split('/')[0]);
  let x_denominator = parseInt(x.split('/')[1]);
  let n_numerator = parseInt(n.split('/')[0]);
  let n_denominator = parseInt(n.split('/')[1]);

  if (x_denominator * n_denominator == n_numerator * x_numerator) {
    return true;
  } else {
    return false;
  }
}



