  let x_numerator = parseInt(x.split('/')[0]);
  let x_denominator = parseInt(x.split('/')[1]);
  let n_numerator = parseInt(n.split('/')[0]);
  let n_denominator = parseInt(n.split('/')[1]);

  return (x_numerator * n_denominator) % (x_denominator * n_numerator) == 0;
}