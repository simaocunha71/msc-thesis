  const x_numerator = parseInt(x.split('/')[0]);
  const x_denominator = parseInt(x.split('/')[1]);
  const n_numerator = parseInt(n.split('/')[0]);
  const n_denominator = parseInt(n.split('/')[1]);

  if (x_denominator * n_denominator == n_numerator * x_numerator) {
    return true;
  }

  return false;
}



