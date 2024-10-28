  if (xs.length % 2 == 1) {
    throw Error('xs must have even number of coefficients')
  }

  var max_coeff = xs[xs.length - 1];
  var min_coeff = xs[0];
  if (max_coeff == 0) {
    throw Error('largest non zero coefficient is expected to be non zero');
  }

  var x_guess = -1.0 * min_coeff / max_coeff;
  var x_points = [];
