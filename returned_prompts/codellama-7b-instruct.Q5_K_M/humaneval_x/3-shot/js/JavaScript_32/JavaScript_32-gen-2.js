  if (xs.length % 2 == 1) {
    throw new Error('Polynomial must have even number of coefficients');
  }
  if (xs[xs.length - 1] == 0) {
    throw new Error('Largest non zero coefficient must be non zero');
  }
  var left = -1;
  var right = 2;
  var epsilon = 1e-9;

  while (right - left > epsilon) {
    var mid = (left + right) / 2;
    if (poly(xs, mid) > 0) {
      right = mid;
    } else {
      left = mid;
    }
  }
  return (left + right) / 2;
}



